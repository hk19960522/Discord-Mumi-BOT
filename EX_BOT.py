import os
import discord

from discord.ext import commands
from discord.ext.commands import Bot

from dotenv import load_dotenv

def TokenReader():
    f = open("Config.txt", "r")
    token = "NONE"
    for context in f:
        if (context.startswith("DISCORD_TOKEN=")):
            token = context[14:]
            break
    return token

#load_dotenv()
#token = os.getenv('DISCORD_TOKEN')
token = TokenReader()

bot = Bot(command_prefix='!')

@bot.command(name='hello')
async def Hello(ctx):
    await ctx.send("HELLO, {}".format(ctx.author.mention))

@bot.command(name='all')
async def TagAll(ctx, context):
    memberRole = discord.utils.get(ctx.guild.roles, name="@everyone")
    await ctx.send(f'{memberRole}, {context}')

bot.run(token)




