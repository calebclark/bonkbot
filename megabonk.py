from handler import Handler
import discord
import config
import util

class MegaBonkHandler(Handler):
    name = "megabonk"

    async def message_handler(self, message, jail, bonkbot):
        print("Starting megabonk handler")
        author = message.author
        # Check if the user can be jailed.
        if not jail.can_jail(author):
            return False
        if self.cf.get("megabonk_trigger_phrase") in message.content.lower() and util.is_mentioned(message, bonkbot):
            await util.send_message(channel, self.cf.get("megabonk_message"))
            for channel in message.guild.channels:
                if channel.id == author.voice.channel.id:
                    print("All members to move = " + str(author.voice.channel.members))
                    for member in author.voice.channel.members:
                        await jail.add(member)
                    return True
        return False
