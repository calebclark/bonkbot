from handler import Handler
import util
import random
import time

class Names(Handler):
    name = "names"
    cooldowns = {}

    async def message_handler(self, message, jail, bonkbot):
        if message.author.id in self.cooldowns:
            print("cooldown comparison: " + str(self.cooldowns[message.author.id]) + ", " + str(time.time()))
        if (not message.author.id in self.cooldowns) or self.cooldowns[message.author.id] < time.time():
            self.cooldowns[message.author.id] = time.time() + 60*60;
            for data in self.cf.get("people"):
                if "|" in data:
                    parts = data.split("|")
                    person = parts[0]
                    alias = random.choice(parts[1:])
                else:
                    person = data
                    alias = person
                if person in util.sanitize(message.content):
                    await message.channel.send(random.choice(self.cf.get("names")).replace("$", alias))
                    return True
        return False
