import os

import discord
from discord.ext import commands
import random
import requests
from time import sleep
intents = discord.Intents()
intents.members = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix = ".", intents = intents)

@bot.event
async def on_ready():
    print("started")
    
@bot.event
async def on_member_join(member):
    print(f'{member.name} joined the server')
    guild = bot.guilds[0]
    welcome = guild.text_channels[0]
    messages = [f'{member.name} Welcome to hell', f'Welcome {member.name} please don\'t enjoy your stay', f'{member.name} Welcome to the shitshow of gяl', f'{member.name} Welcome gяl o/, get your burnt cookies in #shit-talk']
    response = random.choice(messages)
    await welcome.send(response)
    
@bot.command(name="gg", help= "Tell someone to git gud")
async def test(ctx, name):
    await ctx.send("git gud {}".format(name))
    
@bot.command(name='memes', help='Get popular memes')
async def memes(ctx, number):
    url = 'https://meme-api.herokuapp.com/gimme'
    
    if int(number) > 5:
        await ctx.send('Please don\'t ask for that many memes')
    else:
        for x in range(int(number)):
            response = requests.request('GET', url)
            data = response.json()
            await ctx.send('{}'.format(data['url']))
            sleep(1)
    
    
bot.run('Insert Token Here')