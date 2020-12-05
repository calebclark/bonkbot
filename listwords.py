#!/usr/bin/env python3
import discord
import config
import util
from functools import reduce

class ListWordsHandler:
    cf = config.get_instance()

    async def message_handler(self, message, jail, bonkbot):
        print("Starting listwords handler")
        if self.cf.get("list_words_trigger_phrase") in message.content.lower() and util.is_mentioned(message, bonkbot):
            await message.channel.send(util.list_trigger_words())

