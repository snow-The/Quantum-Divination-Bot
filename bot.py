import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=':Q ')

@bot.event
async def on_ready():
    print(">> SQCS-D Bot is online! <<")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{bot.latency*1000}(ms)')

bot.run("OTAwMzUwNDUyMTMzMTM0MzU3.YXACsw.Xl45D1pcU1r8I4wasMVIcGdj3tg")