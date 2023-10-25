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
        if 'https://twitter.com' in message.content:
            await message.channel.send(message.content.replace('https://twitter.com', 'https://vxtwitter.com'))
            await message.delete()
        if 'https://vm.tiktok.com' in message.content:
            r = requests.get(message.content)
            await message.channel.send(r.url.replace('https://www.tiktok.com', 'https://www.vxtiktok.com'))
            await message.delete()
        if 'https://www.tiktok.com' in message.content:
            await message.channel.send(message.content.replace('https://www.tiktok.com', 'https://www.vxtiktok.com'))
            await message.delete()


intents = discord.Intents.default()
intents.message_content = True
client = DiscordClient(intents=intents)
client.run(token)
