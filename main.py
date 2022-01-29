import discord
from discord.ext import commands

import os

import edit_channels
import webhook_utils

intents = discord.Intents.default()
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix="e.", intents=intents)

@bot.event
async def on_ready():
    print("launched")

@bot.event
async def on_message(msg: discord.Message): 
    if msg.channel.id in edit_channels.get_channels_list()[0] and not msg.webhook_id:
        for id in edit_channels.get_linked_channels(msg.channel.id):
            try:
                whook_url = await webhook_utils.create_webhook_if_not_exist(bot, id)
                webhook_utils.send_with_webhook(whook_url, msg.content, msg.guild.name, msg.author.name,  msg.author.avatar_url, msg.attachments)
            except:
                print(f"Error in {id}"}

@bot.event
async def on_message_delete(msg: discord.Message):
    if msg.channel.id in edit_channels.get_channels_list()[0]:
        for id in edit_channels.get_linked_channels(msg.channel.id):
            channel = await bot.fetch_channel(id)
            for msg in await channel.history(limit=10).flatten():
                if msg.content == msg.content:
                    await msg.delete()



bot.run(os.environ["TOKEN"])
