import discord
from discord.ext import commands
import numpy as np 
from qiskit import Aer
from qiskit import *
import asyncio

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
asyncio.get_event_loop().create_task(bot.start('OTAwMzUwNDUyMTMzMTM0MzU3.YXACsw.Trb1rTsTUHPLRdCRESk5q0wRBh0'))