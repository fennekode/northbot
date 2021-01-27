import discord
import os
import asyncio
import logging
import random
from discord.ext import commands

client = discord.Client()

greetings = ["Hey there!", "Heyo!", "Hewwo!", "What's up?", "*bleat*"]


@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

# Ping-pong Command
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  # Simple ping-pong
  if message.content.startswith('~Ping'):
    await message.channel.send('Pong.')

# Greetings
@client.event
async def on_message(message):
  if "northbot" in message.content:
    await message.channel.send(random.choice(greetings))

# Welcome (For esk8 server)
@client.event
async def on_member_join(member):
  # Console new member report
  print("A new member, " + member.name + " has joined.")
  
  # Welcome message
  await client.send_message(discord.Object(id='LOGCHANNEL'), "Welcome, " + member.name + "! Please type \"~verify\" in this channel in order to receive access to this server.")

# Still building a verification system
#@commands.guild_only()
#@client.command(pass_context = True)
@client.event
async def ROLECOMMAND(member):
    role = discord.utils.get(member.guild.roles, name="Verified")
    if role in member.author.roles:
        await member.send('You are already verified')
    else:
        await member.author.add_roles(role)
        await member.send(":white_check_mark: User is now verified!")


client.run(os.getenv('TOKEN'))