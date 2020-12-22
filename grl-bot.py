import random
from time import sleep

import discord
import requests
from discord.ext import commands

from gtts import gTTS

import os
import time

# weird new Intents
# not sure if they are all necessary
intents = discord.Intents()
intents.members = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='.', intents=intents)

#startup message in console
@bot.event
async def on_ready():
    print("started")

#welcome message    
@bot.event
async def on_member_join(member):
    print(f'{member.name} joined the server')
    guild = bot.guilds[0]
    welcome = guild.text_channels[0]
    messages = [f'{member.name} Welcome to hell', f'Welcome {member.name} please don\'t enjoy your stay', 
                f'{member.name} Welcome to the shitshow of gяl', f'{member.name} Welcome gяl o/, get your burnt cookies in #shit-talk']
    response = random.choice(messages)
    await welcome.send(response)

#git gud command    
@bot.command(name='gg', help= 'Tell someone to git gud')
async def test(ctx, name):
    await ctx.send(f'git gud {name}')

#memes command    
@bot.command(name='memes', help='Get popular memes')
async def memes(ctx, number):
    url = 'https://meme-api.herokuapp.com/gimme'

    if int(number) > 5:
        await ctx.send('Please don\'t ask for that many memes')
    else:
        for i in range(int(number)):
            response = requests.request('GET', url)
            data = response.json()
            await ctx.send('{}'.format(data['url']))
            sleep(1)


# insults a grl member
@bot.command(name='insult', help='Insult a grl member')
async def insult(ctx, name):
    insults = open('insults.txt').read().splitlines()
    await ctx.send(f'{name} you {random.choice(insults)}')

# insults a grl member in voice chat
# noinspection SpellCheckingInspection
@bot.command(name='insultvc', help='Insult a grl member in voice chat')
async def insultvc(context, name):
    voice_channel = context.author.channel
    if voice_channel is not None:
        # text to speech and save as mp3
        insults = open('insults.txt').read().splitlines()
        audio = gTTS(text=f'{name.replace("@", "")} you {random.choice(insults)}', lang='en', slow=False)
        filename = 'insult-' + str(time.time()) + '.mp3'
        audio.save(filename)

        # connect to vc und play audio
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(filename))
        # Sleep while audio is playing.
        while vc.is_playing():
            sleep(.5)
        # disconnect from vc and delete mp3 file
        await vc.disconnect()
        os.remove(filename)
    else:
        await context.send(f'Please connect to a voice channel first. You {insult}')

f = open('token.txt', 'r')
token = f.read()
bot.run(token)
