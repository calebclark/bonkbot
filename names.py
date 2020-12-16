from handler import Handler
import util
import random

class Names(Handler):
    name = "names"

    async def message_handler(self, message, jail, bonkbot):
        for person in self.cf.get("people"):
            if person in util.sanitize(message.content):
                await message.channel.send(person + " " + random.choice(self.cf.get("names")))
                return True
        return False
