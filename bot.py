import discord
from discord.ext import commands
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi
from qiskit import Aer
from qiskit import *
from qiskit.providers.aer import QasmSimulator
import asyncio
bot = commands.Bot(command_prefix='Q:')
#normal_and_start
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)
circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.p(1.5, qreg_q[0])
circuit.h(qreg_q[0])
circuit.barrier(qreg_q[0], qreg_q[1])
circuit.p(1.5, qreg_q[1])
circuit.h(qreg_q[1])
circuit.barrier(qreg_q[1], qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])
backend = QasmSimulator()
qc = circuit.compose(circuit, range(2), front=True)
qc_compiled = transpile(qc, backend)
job_sim = backend.run(qc_compiled, shots=6144)
#1to0
qreg_q1_0 = QuantumRegister(2, 'q')
creg_c1_0 = ClassicalRegister(2, 'c')
circuit1_0 = QuantumCircuit(qreg_q1_0, creg_c1_0)
circuit1_0.h(qreg_q1_0[0])
circuit1_0.h(qreg_q1_0[1])
circuit1_0.p(1.5, qreg_q1_0[0])
circuit1_0.h(qreg_q1_0[0])
circuit1_0.barrier(qreg_q1_0[0], qreg_q1_0[1])
circuit1_0.p(1.5, qreg_q1_0[1])
circuit1_0.h(qreg_q1_0[1])
circuit1_0.barrier(qreg_q1_0[1], qreg_q1_0[0])
circuit1_0.cx(qreg_q1_0[1], qreg_q1_0[0])
circuit1_0.measure(qreg_q1_0[0], creg_c1_0[0])
circuit1_0.measure(qreg_q1_0[1], creg_c1_0[1])
#0to1
qreg_q0_1 = QuantumRegister(2, 'q')
creg_c0_1 = ClassicalRegister(2, 'c')
circuit0_1 = QuantumCircuit(qreg_q0_1, creg_c0_1)
circuit0_1.h(qreg_q0_1[0])
circuit0_1.h(qreg_q0_1[1])
circuit0_1.p(1.5, qreg_q0_1[0])
circuit0_1.h(qreg_q0_1[0])
circuit0_1.barrier(qreg_q0_1[0], qreg_q0_1[1])
circuit0_1.p(1.5, qreg_q0_1[1])
circuit0_1.h(qreg_q0_1[1])
circuit0_1.barrier(qreg_q0_1[1], qreg_q0_1[0])
circuit0_1.cx(qreg_q0_1[0], qreg_q0_1[1])
circuit0_1.measure(qreg_q0_1[0], creg_c0_1[0])
circuit0_1.measure(qreg_q0_1[1], creg_c0_1[1])

@bot.event
async def on_ready():
    print(">> SQCS-D Bot is online! <<")
@bot.command()
async def normal(ctx):
    backend = QasmSimulator()
    qc = circuit.compose(circuit, range(2), front=True)
    qc_compiled = transpile(qc, backend)
    job_sim = backend.run(qc_compiled, shots=6144)
    await ctx.send("normal mode!")
@bot.command()
async def cnot1to0(ctx):
    backend = QasmSimulator()
    qc = circuit1_0.compose(circuit1_0, range(2), front=True)
    qc_compiled = transpile(qc, backend)
    job_sim = backend.run(qc_compiled, shots=6144)
    await ctx.send("1to0 mode")
@bot.command()
async def cnot0to1(ctx):
    backend = QasmSimulator()
    qc = circuit0_1.compose(circuit0_1, range(2), front=True)
    qc_compiled = transpile(qc, backend)
    job_sim = backend.run(qc_compiled, shots=6144)
    await ctx.send("0to1 mode")
@bot.command()
async def shot(ctx):
    result_sim = job_sim.result()
    counts = result_sim.get_counts(qc_compiled)
    await ctx.send(counts)
@bot.command()
async def jiaobei(ctx):
    await ctx.send("Pray to quantum god for your mind!")
    for i in range(3):
        job_sim = backend.run(qc_compiled, shots=6144)
        result_sim = job_sim.result()
        counts = result_sim.get_counts(qc_compiled)
        mx=counts['00']
        if mx <= counts['10']:
            mx=counts['10']
        if mx <= counts['01']:
            mx=counts['01']
        if mx <= counts['11']:
            mx=counts['11']
        #next
        if mx == counts['00']:
            await ctx.send("laughing answer")
        elif mx == counts['10']:
            await ctx.send("divine answer")
        elif mx == counts['01']:
            await ctx.send("divine answer")
        elif mx == counts['11']:
            await ctx.send("angry answer")
asyncio.get_event_loop().create_task(bot.start('your token'))
