#gets stuff to make bot (pulling necessary info)
import discord
import os
 
from discord.ext import commands
 
#holds the instance of our bot
client = commands.Bot(command_prefix = ".")
 
#Event - code that executes when the bot detects something in particular
 
#on_Ready function executes code when your bot is rdy to use
@client.event
async def on_ready():
    print("IM READY!")
 
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')
 
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')
 
 
#Token/API Key - a code that connects our code to our bot (if someone takes this u are screwed)
client.run(os.environ.get('TOBOT'))
