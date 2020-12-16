from handler import Handler
import discord
import util

class BonkHandler(Handler):
    name = "bonk"

    async def message_handler(self, message, jail, bonkbot):
        author = message.author
        # Check if the user can be jailed.
        if not jail.can_jail(author):
            return False

        for word in self.cf.get("trigger_words"):
            if word in util.sanitize(message.content).split():
                await jail.add(author)
                await message.channel.send(self.cf.get("jail_message"))
                return True 
        return False
