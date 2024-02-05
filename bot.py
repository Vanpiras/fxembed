import os
import random
import discord

f = open('.token')
token = f.read().strip()

insultes = [ "Nique ta mère", "Ta grosse daronne la chienne", "Grosse pute", "je te déteste", "t'es ban", "/ban", "bachi-bouzouk", "ta putain de race de merde"]

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
            await message.channel.send(prefix + message.content.replace('https://vm.tiktok.com', 'https://vm.vxtiktok.com'), silent=True)
            await message.delete()
        if 'https://www.tiktok.com' in message.content:
            await message.channel.send(prefix + message.content.replace('https://www.tiktok.com', 'https://www.vxtiktok.com'), silent=True)
            await message.delete()
        if 'https://instagram.com' in message.content:
            await message.channel.send(prefix + message.content.replace('https://instagram.com', 'https://ddinstagram.com'), silent=True)
            await message.delete()
        if message.content == 'feur' or message.content == "Feur" or message.content.endswith(" feur"):
            await message.channel.send(insultes[random.randint(0, len(insultes) - 1)])


intents = discord.Intents.default()
intents.message_content = True
client = DiscordClient(intents=intents)
client.run(token)
