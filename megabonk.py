#!/usr/bin/env python3
import discord
import config
import util

class MegaBonkHandler:
    cf = config.get_instance()

    async def message_handler(self, message, jail, bonkbot):
        print("Starting megabonk handler")
        author = message.author
        # Check if the user can be jailed.
        if not jail.can_jail(author):
            return
        if self.cf.get("megabonk_trigger_phrase") in message.content.lower() and util.is_mentioned(message, bonkbot):
            await message.channel.send(self.cf.get("megabonk_message"))
            for channel in message.guild.channels:
                if channel.id == author.voice.channel.id:
                    print("All members to move = " + str(author.voice.channel.members))
                    for member in author.voice.channel.members:
                        await jail.add(member)
                    return
