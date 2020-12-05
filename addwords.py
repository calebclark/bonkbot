#!/usr/bin/env python3
import config
import util
import discord.utils

class AddWordsHandler:
    cf = config.get_instance()

    async def message_handler(self, message, jail, bonkbot):
        print("Starting add words handler")
        if not util.is_mentioned(message, bonkbot):
            return
        print("Bonk bot was mentioned")
        command_words = util.sanitize(discord.utils.escape_mentions(message.content)).split()
        print("command_words = " + str(command_words))
        prefix = command_words[0] + " " + command_words[1]
        trigger = self.cf.get("add_words_trigger_phrase") 
        print("comparing " +  prefix + " and " + trigger)
        if prefix == trigger or prefix + "s" == trigger:
            print("add words command was present")
            new_list = sorted(list(set(self.cf.get("trigger_words")).union(set(command_words[2:]))))
            self.cf.put("trigger_words", new_list)
            await message.channel.send(util.list_trigger_words())
            
            

