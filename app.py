from multiprocessing import context
from time import sleep
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
import os
import asyncio

load_dotenv()

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(name='boca')
async def boca(ctx):
    await entraBot(ctx, "sounds/cala.ogg", 3)

@bot.command(name='cu')
async def cu(ctx):
    await entraBot(ctx, "sounds/cu.ogg", 4)

@bot.command(name='rato')
async def rato(ctx):
    await entraBot(ctx, "sounds/rato.ogg", 4)

@bot.command(name='pegadinha')
async def pegadinha(ctx):
    await entraBot(ctx, "sounds/pegadinha.ogg", 5)

@bot.command(name='chernobyl')
async def chernobyl(ctx):
    await entraBot(ctx, "sounds/chernobyl.ogg", 4)

@bot.command(name='vergonha')
async def vergonha(ctx):
    await entraBot(ctx, "sounds/vergonha.ogg", 4)

@bot.command(name='pegou')
async def pegou(ctx):
    await entraBot(ctx, "sounds/pegou.ogg", 4)

@bot.command(name='culpa')
async def culpa(ctx):
    await entraBot(ctx, "sounds/culpa.ogg", 4)


async def entraBot(ctx, song, tempo):
    voiceChannel = discord.utils.get(ctx.guild.channels)
    vc = await voiceChannel.connect()
    vc.play(FFmpegPCMAudio(song), after=None)
    sleep(tempo)
    await ctx.voice_client.disconnect()


bot.run(os.getenv("TOKEN"))