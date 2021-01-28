#!/usr/bin/env python3
import discord
import config
import util

class Yikes:
    cf = config.get_instance()    

    async def message_handler(self, message, jail, bonkbot):
        if message.channel.name == "yikes":
            await message.delete(delay = 60*60)
