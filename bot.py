import discord
from dotenv import load_dotenv
from os import getenv
load_dotenv(override=True)

client = discord.Client()

from main import process

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    response = process[msg.content]
    if response:
        await msg.channel.send(response)

@client.event
async def on_ready():
    print("hello!")

client.run(getenv("TOKEN"))
    
