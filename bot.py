# bot.py
import os
import io
import aiohttp
# import vlc

import discord
from discord import FFmpegPCMAudio, player
from discord.ext import commands
# from dotenv import load_dotenv

DISCORD_TOKEN = 'Nzg1NDEyMzc3MzI3MTczNjM4.X83eRw.OE6QXoIRsgIHvziB_LKmbPlhsus'
client = discord.Client()
BOT_PREFIX = '$'

bot = commands.Bot(command_prefix=BOT_PREFIX)
# DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


@bot.command()
async def find(ctx, arg1):
    IMAGE = 'https://img.pokemondb.net/sprites/x-y/normal/' + arg1 + '.png'
    print(IMAGE)
    async with aiohttp.ClientSession() as session:
        async with session.get(IMAGE) as resp:
            if resp.status != 200:
                return await ctx.send('No such pokemon!')
            data = io.BytesIO(await resp.read())
            await ctx.send(file=discord.File(data, arg1+'.png'))

@bot.command(aliases=['listen'])
async def hear(ctx, arg1):
    author = ctx.message.author
    channel = author.voice.channel
    voice = await channel.connect()

    source = 'https://play.pokemonshowdown.com/audio/cries/' + arg1 + '.mp3'

    global player
    try:
        player = await channel.connect()
    except:
        pass
    player.play(FFmpegPCMAudio(source))


@bot.command(aliases=['s', 'sto'])
async def stop(ctx):
    await ctx.message.author.voice.channel.connect().disconnect()

# @client.event
# async def on_ready():
#    print('We have logged in as {0.user}'.format(client))
bot.run(DISCORD_TOKEN)