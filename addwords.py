#!/usr/bin/env python3
import config
import util
import discord.utils
from handler import Handler

class AddWordsHandler(Handler):
    name = "addwords"

    def matches(self, message, bonkbot, command_words):
        if not util.is_mentioned(message, bonkbot):
            return
        prefix = command_words[0] + " " + command_words[1]
        trigger = self.cf.get("add_words_trigger_phrase") 
        return prefix == trigger or prefix + "s" == trigger

    async def message_handler(self, message, jail, bonkbot):
        command_words = util.sanitize(discord.utils.escape_mentions(message.content)).split()
        if self.matches(message, bonkbot, command_words):
            new_list = sorted(list(set(self.cf.get("trigger_words")).union(set(command_words[2:]))))
            self.cf.put("trigger_words", new_list)
            await message.channel.send(util.list_trigger_words())
            return True
        return False
