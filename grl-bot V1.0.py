import random
from time import sleep

import discord
import requests
from discord.ext import commands

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


f = open('token.txt', 'r')
token = f.read()
bot.run(token)
