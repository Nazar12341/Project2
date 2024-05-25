import discord
import random
from discord.ext import commands
from random import randint

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.command('kydavibrasivat')
async def kydavibrasivat(ctx):
    with open('images/image2.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('skolkoraslogaetsa')
async def skolkoraslogaetsa(ctx):
    with open('images/image3.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('mojnovibrasivat')
async def mojnovibrasivat(ctx):
    with open('images/image.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("token") 
