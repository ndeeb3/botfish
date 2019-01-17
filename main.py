import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

import json
import random

with open("auth.json", "r") as read_file:
    data = json.load(read_file)
TOKEN = data["token"] # authorization token
bot = discord.Client()

pings = ["<@&402527268678795264>", "<@&522663886411923456>", "<@&532423760289202177>"]
ping_formats = [
    "anyone up? 🙋‍ {}",
    "wow your memeing is so fucking funny {} like this is the pinnacle of memery hahahaha did i ever tell you that you're so funny for pointing out little quirky things like that hahahaah {}"
    "lmfaoroflXDlol {}",
    "Hi hungry, I'm dad {}",
    "You're welcome, {}!"]

@bot.event
async def on_message(message):
    if any(map(lambda p: p in message.content, pings)):
        channels = list(filter(lambda c: str(c.type) == "text", message.server.channels))
        channelsToPing = random.sample(channels, int(len(channels)/2))
        for c in channelsToPing:
            ping_message = await bot.send_message(c, random.choice(ping_formats).format(message.author.mention))
            await bot.delete_message(ping_message)
            await asyncio.sleep(random.randint(5, 15))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)
bot.close()
