import os
import random
import discord
import re

f = open('.token')
token = f.read().strip()

insultes = ["Nique ta mère", "Ta grosse daronne la chienne", "Grosse pute", "je te déteste", "t'es ban", "/ban", "bachi-bouzouk", "ta putain de race de merde"]

banlist = ["feur", "coubeh", "apagnan"]

def is_banlisted(msg):
    for word in banlist:
        if word in msg:
            return True
    return False

def is_bypass(msg):
    return "!bypass " in msg

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if is_bypass(message.content):
            return
        prefix = f"<@{message.author.id}> sent:\n" 
        if 'https://twitter.com' in message.content:
            if re.match("https:\/\/twitter.com\/(.*\/)+", message.content):
                await message.channel.send(prefix + message.content.replace('https://twitter.com', 'https://vxtwitter.com'), silent=True)
                await message.delete()
        if 'https://x.com' in message.content:
            if re.match("https:\/\/x.com\/(.*\/)+", message.content):
                await message.channel.send(prefix + message.content.replace('https://x.com', 'https://fixvx.com'), silent=True)
                await message.delete()
        if 'https://vm.tiktok.com' in message.content:
            await message.channel.send(prefix + message.content.replace('https://vm.tiktok.com', 'https://vm.vxtiktok.com'), silent=True)
            await message.delete()
        #if 'https://www.tiktok.com' in message.content:
            #await message.channel.send(prefix + message.content.replace('https://www.tiktok.com', 'https://www.vxtiktok.com'), silent=True)
            #await message.delete()
        if 'https://instagram.com' in message.content:
            await message.channel.send(prefix + message.content.replace('https://instagram.com', 'https://ddinstagram.com'), silent=True)
        if 'https://clips.twitch.tv' in message.content:
            await message.channel.send(prefix + message.content + "??????????????????????????ntmtwitch", silent=True)
            await message.delete()
        low = message.content.lower()
        if is_banlisted(low):
            for word in banlist:
                if low.startswith(word) or low.endswith(" " + word) or (" " + word + " ") in low:
                    await message.channel.send(insultes[random.randint(0, len(insultes) - 1)])


intents = discord.Intents.default()
intents.message_content = True
client = DiscordClient(intents=intents)
client.run(token)
