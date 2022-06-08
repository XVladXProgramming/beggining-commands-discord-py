import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='X')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('TOKEN YOUR BOT')


//example by https://github.com/XVladXProgramming/beggining-commands-discord-py/tree/main
