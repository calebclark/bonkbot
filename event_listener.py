#!/usr/bin/env python3
import discord
import secrets
import bonk
import megabonk
import listwords
import addwords
import deletewords
import util
import jail

intent = discord.Intents.all()
client = discord.Client(intents = intent)

handlers = [bonk.BonkHandler(), megabonk.MegaBonkHandler()] 
command_handlers = [listwords.ListWordsHandler(), addwords.AddWordsHandler(), deletewords.DeleteWordsHandler()]


@client.event
async def on_message(message):
    print(str(message))
    print(str(client.user.id))
    bonkbot = client.user 
    # Don't react to our own messages.
    if message.author == client.user:
        return
    print(message.content)
    guild_jail = jail.Jail(message.guild)
    for handler in handlers:
        await handler.message_handler(message, guild_jail, bonkbot)
    if not util.in_bot_channel(message):
        return
    for handler in command_handlers:
        await handler.message_handler(message, guild_jail, bonkbot)

client.run(secrets.get_discord_token())
