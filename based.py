from handler import Handler
import util

class Based(Handler):
    name = "names"
    cooldowns = {}
    def __init__(self, client):
        self.client = client

    async def message_handler(self, message, jail, bonkbot):
        #await self.client.user.edit(username="Based Bot")
        if util.sanitize(message.content) == "based":
            await message.channel.send("based")
            return True
        return False
