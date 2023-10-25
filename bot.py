import os
import discord
import requests

f = open('.token')
token = f.read().strip()

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        prefix = f"<@{message.author.id}> sent:\n" 
        if 'https://twitter.com' in message.content:
            await message.channel.send(prefix + message.content.replace('https://twitter.com', 'https://vxtwitter.com'), silent=True)
            await message.delete()
        if 'https://vm.tiktok.com' in message.content:
            r = requests.get(message.content)
            await message.channel.send(prefix + r.url.replace('https://www.tiktok.com', 'https://www.vxtiktok.com'), silent=True)
            await message.delete()
        if 'https://www.tiktok.com' in message.content:
            await message.channel.send(prefix + message.content.replace('https://www.tiktok.com', 'https://www.vxtiktok.com'), silent=True)
            await message.delete()
        if 'https://instagram.com' in message.content:
            await message.channel.send(prefix + message.content.replace('https://instagram.com', 'https://ddinstagram.com'), silent=True)
            await message.delete()


intents = discord.Intents.default()
intents.message_content = True
client = DiscordClient(intents=intents)
client.run(token)
