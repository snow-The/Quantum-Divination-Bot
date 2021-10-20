import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='Q:')

@bot.event
async def on_ready():
    print(">> SQCS-D Bot is online! <<")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{bot.latency*1000}(ms)')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

bot.run('')