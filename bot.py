# bot.py
import os
import io
from time import sleep
import aiohttp
import asyncio

# PokeDex API wrapper
import pokebase as pb
from pokebase import cache

import discord
from discord import FFmpegPCMAudio, player
from discord.ext import commands
# from dotenv import load_dotenv

DISCORD_TOKEN = 'Nzg1NDEyMzc3MzI3MTczNjM4.X83eRw.OE6QXoIRsgIHvziB_LKmbPlhsus'
client = discord.Client()
DISCORD_TOKEN_UNLUCKYGOLEM = 'Nzg5MTYxNzc5MDY1MjU4MTA0.X9uCLg.HOYnxmq2nzarwN3RaViOPd_GBQI'
BOT_PREFIX = '$'
cache.API_CACHE

''' 
######### POKEBASE API USAGE ##########
pokemon = pb.pokemon(pokemon)
<pokemon>.<attribute> // retrieves <attribute>
attribute(s): name; natural_gift_type; height; weight

source = pb.SpriteResource('pokemon', 17)
source.url
source.img_data
'''

bot = commands.Bot(command_prefix=BOT_PREFIX)
    # DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


@bot.command(aliases=['encounter'])
async def find(ctx, arg1):
    if arg1 == 'yourmom':
        arg1 = 'snorlax'
    POKEMON = pb.pokemon(arg1)
    IMAGE = pb.SpriteResource('pokemon', POKEMON.id)
    IMAGE_URL = IMAGE.url
    IMAGE_FILE = './sprites/pokemon' + str(POKEMON.id) + ".png"
    async with aiohttp.ClientSession() as session:
        async with session.get(IMAGE_URL) as resp:
            if resp.status != 200:
                return await ctx.send('No such pokemon!')
            data = io.BytesIO(await resp.read())
            await ctx.send(file=discord.File(data, IMAGE_FILE))

@bot.command(aliases=['listen', 'cry'])
async def hear(ctx, arg1):
    if arg1 == 'yourmom':
        arg1 = 'snorlax'
    POKEMON = pb.pokemon(arg1)
    MEDIA_URL = 'https://veekun.com/dex/media/pokemon/cries/' + str(POKEMON.id) + '.ogg'
    MEDIA_FILE = './cries/' + str(POKEMON.id) + '.ogg'

    channel = ctx.message.author.voice.channel
    vc = await channel.connect(reconnect=False)
    sleep(.5)
    vc.play(discord.FFmpegPCMAudio(MEDIA_FILE))
    vc.cleanup()
    sleep(5)
    await vc.disconnect()


@bot.command(aliases=['s', 'leave'])
async def stop(ctx):
    await ctx.message.author.voice.channel.disconnect(force=True)

# @client.event
# async def on_ready():
#    print('We have logged in as {0.user}'.format(client))
bot.run(DISCORD_TOKEN_UNLUCKYGOLEM)