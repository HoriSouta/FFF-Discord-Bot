import json

import nextcord
from nextcord.ext import commands
import time
import asyncio

#Allow for commands to work
intents = nextcord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='t!',intents=intents)

players = []
savesplayer = []
startgame = None
starttimer = 0
answer = ''
token = 1
strictmode = True
channelid = 0

with open('config.json') as f:
    data = json.load(f)

token = data['token']
strictmode = data['Strict mode']
channelid = data['Channel']

def removetext(text):
    tebu = str(text)
    tebu = tebu.lower()
    texts = tebu.replace(' ','')
    return texts

@client.event
async def on_ready():
    print('Bot is ready!')


@client.command()

async def add(ctx, user: nextcord.Member, *, message=None):
    message = 'Your are the contestant who will play in FFF round, goodluck!'
    warn = 'Computer will only accept your answer if your answer only have 4 letters \'abcd\''
    embed = nextcord.Embed(title=message, color=0xfff700)
    players.append(user.id)
    await ctx.send(f'Add player{user.mention}')
    await user.send(embed=embed)
    if strictmode:
        await user.send(warn)
    print(players)

@client.command()
async def list(ctx):
    await ctx.send('List of player')
    for x in players:
        user = await ctx.guild.query_members(user_ids=[x])  # list of members with userid
        user = user[0]  # there should be only one so get the first item in the list
        await ctx.send(f'{user.mention}')


@client.command()
async def remove(ctx, user: nextcord.Member, *, message=None):
    players.remove(user.id)
    await ctx.send(f'Removing {user.mention}')

@client.command()
async def answer(ctx, ans:str):
    global answer
    answer = ans.lower()
    await ctx.send(f'The answer for this turn is: {answer}')


@client.command()
async def channel(ctx, channel : nextcord.TextChannel):
    global channelid
    channelid = channel.id
    await ctx.send(f'Log channel will be in: {channel.mention}')

@client.command()
async def test(ctx, message=None):
    message = 'This message is to check if the bot is working!'
    embed = nextcord.Embed(title=message, color=0xfff700)
    for x in players:
        user = await ctx.guild.query_members(user_ids=[x])  # list of members with userid
        user = user[0]  # there should be only one so get the first item in the list
        await user.send(embed=embed)


@client.command()
async def save(ctx, message=None):
    message = 'Saving player list'
    embed = nextcord.Embed(title=message, color=0xfff700)
    global savesplayer
    savesplayer = players.copy()
    await ctx.send(embed=embed)


@client.command()
async def load(ctx, message=None):
    message = 'Loading player list'
    embed = nextcord.Embed(title=message, color=0xfff700)
    global players
    players = savesplayer.copy()
    await ctx.send(embed=embed)


@client.command()
async def start(ctx, message=None):
    global starttimer
    global startgame
    starttimer = time.time()
    startgame = True

    message = 'The time has been started, you now can answer the question'
    embed = nextcord.Embed(title=message,color=0x11ff00)
    for x in players:
        user = await ctx.guild.query_members(user_ids=[x])  # list of members with userid
        user = user[0]  # there should be only one so get the first item in the list
        await user.send(embed=embed)

    global savesplayer
    savesplayer = players.copy()

    await asyncio.sleep(20)
    startgame = False

    message = 'Time is up! You can not answer the question any more'
    embed = nextcord.Embed(title=message, color=0xff0000)

    for x in savesplayer:
        user = await ctx.guild.query_members(user_ids=[x])  # list of members with userid
        user = user[0]  # there should be only one so get the first item in the list
        await user.send(embed=embed)


@client.command()
async def timeleft(ctx, message=None):
    message = f'Thời gian còn lại là: {time.time()-starttimer}'
    embed = nextcord.Embed(title=message)
    await ctx.send(embed=embed)


@client.event
async def on_message(message):
    finaltime = "{:.2f}".format(time.time() - starttimer)
    text = message.content

    if message.channel.type == nextcord.ChannelType.private and message.author.id in players and startgame is True:

        texts = removetext(text)
        players.remove(message.author.id)
        channel = client.get_channel(channelid)
        embedsee = nextcord.Embed(title='Computer has recive your answer', color=0x11ff00)
        await message.channel.send(embed=embedsee)

        if texts == answer and strictmode:
            embedlog = nextcord.Embed(title=f'Player{message.author.name} answered correctly in {finaltime}',color=0x11ff00)
            await channel.send(embed=embedlog)
        elif not strictmode:
            embedlog = nextcord.Embed(title=f'Player {message.author.name} answered in {finaltime} with the answer is {texts}',color=0x11ff00)
            await channel.send(embed=embedlog)

    await client.process_commands(message)

client.run(token)
