from time import sleep
import discord
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
import os

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$boca'):
        channel = message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('cala.ogg')
        player = voice.play(source)
        
        
client.run(os.getenv("TOKEN"))