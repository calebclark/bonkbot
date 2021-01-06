from handler import Handler
import util

bad_author_ids = ['224430256361177088']

class Based(Handler):
    name = "names"
    cooldowns = {}
    def __init__(self, client):
        self.client = client

    async def message_handler(self, message, jail, bonkbot):
        #await self.client.user.edit(username="Based Bot")
        if util.sanitize(message.content) == "based":
            if message.author.id in bad_author_ids:
                response = "not based"
            else:
                response = "based"
            await message.channel.send(response)
            return True
        return False
