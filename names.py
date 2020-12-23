from handler import Handler
import util
import random

class Names(Handler):
    name = "names"

    async def message_handler(self, message, jail, bonkbot):
        if random.randrange(5) == 0:
            for person in self.cf.get("people"):
                if person in util.sanitize(message.content):
                    await message.channel.send(random.choice(self.cf.get("names")).replace("$", person))
                    return True
        return False
