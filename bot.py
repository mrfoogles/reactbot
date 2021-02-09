import discord
import os
from main import process

from http import server

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        print("Hello!")

    async def on_message(self,msg):
        if msg.author == client.user:
            return

        response = process(msg.content)
        if response:
            await msg.channel.send(response)

from server import keep_alive
keep_alive()

client = MyClient()
client.run(os.getenv("TOKEN"))