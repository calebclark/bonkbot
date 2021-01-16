from handler import Handler
import util
import random
import time

class Names(Handler):

    async def message_handler(self, message, jail, bonkbot):
        for data in self.cf.get("people"):
            if "|" in data:
                parts = data.split("|")
                person = parts[0]
                alias = random.choice(parts[1:])
            else:
                person = data
                alias = person
            if person in util.sanitize(message.content):
                await util.send_message(message.channel, random.choice(self.cf.get("names")).replace("$", alias))
                return True
        return False
