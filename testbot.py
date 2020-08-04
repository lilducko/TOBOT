#gets stuff to make bot (pulling necessary info)
import discord
import os
import random
 
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import Bot
 
#holds the instance of our bot
client = commands.Bot(command_prefix = ".")
 
#Event - code that executes when the bot detects something in particular
 
#on_Ready function executes code when your bot is rdy to use

status = cycle(['Big bro is stocking,' 'im still creeping on you', 'XXXAfro_DennisXXX is spying on you'])
@client.event
async def on_ready():
    print("IM READY!")
    await client.change_presence(status=discord.Status.idle,)
    change_status.start()

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')
 
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')

#code that runs ehrn a user tells the bot to do something
@client.command(aliases = ['8ball', 'balls'])
async def _8ball(ctx, *, question):
    responses = ["Yes","No","Maybe"]
    await ctx.send(f'Question: {question} \n Answer: {random.choice(responses)}')
 
@client.command()
async def clear(ctx, amount = 3):
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    #add asstrix(*) to make the question estack into the reason parameteru
    await member.kick(reason = reason)




#Token/API Key - a code that connects our codur bot (if someone takes this u are screwed)

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"Banned {member.mention}")
#my code
# client.command(aliases = ['8ball', 'balls'])
# async def _8ball(ctx, *, question):
#     responses = ["shiz","frik","fudge","jeez"]
#     for badWord in responses:
#         if(badWord in bad_entry):
#         await ctx.send("Watch your language!")
#         return
#my code
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminatior = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminatior):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {member.mention}")
            return
@tasks.loop(seconds = 5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


#Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command! Please try again!")

client.run(os.environ.get('TOBOT'))