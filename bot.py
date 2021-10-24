import discord
from discord.ext import commands
import numpy as np 
from qiskit import Aer
from qiskit import *
import asyncio
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi
from qiskit import transpile
from qiskit.providers.aer import QasmSimulator
bot = commands.Bot(command_prefix='Q:')

circ = QuantumCircuit(3)
circ.h(0)
circ.cx(0, 1)
circ.cx(0, 2)
meas = QuantumCircuit(3, 3)
meas.barrier(range(3))
meas.measure(range(3), range(3))
circ.add_register(meas.cregs[0])
qc = circ.compose(meas)
backend_sim = Aer.get_backend('qasm_simulator')

qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.p(1.5, qreg_q[0])
circuit.h(qreg_q[0])
circuit.barrier(qreg_q[0], qreg_q[1])
circuit.p(1.5, qreg_q[1])
circuit.h(qreg_q[1])
circuit.ccx(qreg_q[1], qreg_q[2], qreg_q[3])
circuit.ccx(qreg_q[0], qreg_q[2], qreg_q[3])
circuit.barrier(qreg_q[1], qreg_q[0], qreg_q[2], qreg_q[3])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[2], creg_c[2])
circuit.measure(qreg_q[3], creg_c[3])
backend_1 = QasmSimulator()
qc_1 = circuit.compose(circuit, range(4), front=True)
qc_compiled_1 = transpile(qc_1, backend_1)

@bot.event
async def on_ready():
    print(">> SQCS-D Bot is online! <<")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{bot.latency*1000}(ms)')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def use(ctx):
    job_sim = backend_sim.run(transpile(qc, backend_sim), shots=4096)
    result_sim = job_sim.result()
    counts = result_sim.get_counts(qc)
    ab= str(counts).split(" ")
    await ctx.send(counts)
    if(ab[1][0:4]>ab[3][0:4]):
        await ctx.send(f'反面')
    elif(ab[1][0:4]<ab[3][0:4]):
        await ctx.send(f'正面')
    else:
        await ctx.send('正反面')
@bot.command()
async def useD(ctx):
    await ctx.send('在心中向量子神告訴你的個人資料')
    await ctx.send('心要誠懇，擲筊才會靈啦！')
    await ctx.send('來啦，開始了')
    abcd=[[], [], []]
    j=['0','0','0']
    for i in range(3):
        job_sim_1 = backend_1.run(qc_compiled_1, shots=6144)
        result_sim_1 = job_sim_1.result()
        counts_1 = result_sim_1.get_counts(qc_compiled_1)
        abcd[i]= str(counts_1).split(" ")
        await ctx.send(counts_1)
        if abcd[i][3][0:4] >= abcd[i][5][0:4]:
            abcd[i][5]=abcd[i][3]
        else:
            abcd[i][5]=abcd[i][3]
        if abcd[i][1][0:4] > abcd[i][3][0:4] and abcd[i][1][0:4] > abcd[i][7][0:4]:
            await ctx.send('聖筊')
            j[i]=0
        elif abcd[i][1][0:4]==abcd[i][3][0:4] and abcd[i][1][0:4]==abcd[i][7][0:4]:
            await ctx.send('大三元啦，聖筊+笑筊+陰筊')
        elif abcd[i][1][0:4] == abcd[i][3][0:4]:
            await ctx.send('聖筊+笑筊')
        elif abcd[i][1][0:4] == abcd[i][7][0:4]:
            await ctx.send('聖筊+陰筊')
        elif abcd[i][3][0:4] > abcd[i][7][0:4]:
            await ctx.send('笑筊')
        elif abcd[i][3][0:4] == abcd[i][7][0:4]:
            await ctx.send('笑筊+陰筊')
        elif abcd[i][7][0:4] > abcd[i][3][0:4] and abcd[i][7][0:4] > abcd[i][1][0:4]:
            await ctx.send('陰筊')
        else:
            await ctx.send('我看不到啦')
    await ctx.send('看到了吧，你有什麽打算就相信自己')
    await ctx.send('沒有事我回去吃下午茶了,Bye!')
    if j[0]==1 and j[1]==1 and j[2]==1:
        await ctx.send('我有黑箱，你很勇麽，居然可以用我的後門。')

asyncio.get_event_loop().create_task(bot.start(''))