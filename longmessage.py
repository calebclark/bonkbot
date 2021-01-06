from handler import Handler
import random

class LongMessageHandler(Handler):
    name = "longmessage"

    def matches(self, message, bonkbot):
        return len(message.content) >= self.cf.get("long_message_length")

    async def message_handler(self, message, jail, bonkbot):
        if self.matches(message, bonkbot):
            await message.channel.send(random.choice(self.cf.get("long_message_responses")))
            return True 
        return False
