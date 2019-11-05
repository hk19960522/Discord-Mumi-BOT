import os
import discord

from discord.ext import commands
from discord.ext.commands import Bot


from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = Bot(command_prefix='!')

@bot.command(name='hello')
async def Hello(ctx):
    await ctx.send("HELLO, {}".format(ctx.author.mention))

@bot.command(name='all')
async def TagAll(ctx, context):
    memberRole = discord.utils.get(ctx.guild.roles, name="@everyone")
    await ctx.send(f'{memberRole}, {context}')

bot.run(token)