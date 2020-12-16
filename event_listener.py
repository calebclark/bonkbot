#!/usr/bin/env python3
import discord
import secrets
import bonk
import megabonk
import listwords
import addwords
import deletewords
import longmessage
import util
import jail
import names

intent = discord.Intents.all()
client = discord.Client(intents = intent)

handlers = [names.Names(), bonk.BonkHandler(), megabonk.MegaBonkHandler(), longmessage.LongMessageHandler()] 
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
    if util.in_bot_channel(message):
        for handler in command_handlers:
            if await handler.message_handler(message, guild_jail, bonkbot):
                return
    for handler in handlers:
        if await handler.message_handler(message, guild_jail, bonkbot):
            return

client.run(secrets.get_discord_token())
