import re
import config
from functools import reduce

def is_mentioned(message, user):
    nickname_mention = '<@!' + str(user.id) + '>'
    mention = '<@' + str(user.id) + '>'
    return mention in message.content or nickname_mention in message.content

def sanitize(string):
    return re.sub('[^\sa-z]', '',string.lower())

def list_trigger_words():
    return reduce(lambda x, y: x + ", " + y, config.get_instance().get("trigger_words")) 
def in_bot_channel(message):
    return message.channel.name == config.get_instance().get("bot_channel")

async def send_message(channel, text):
    await channel.send(text, delete_after=60)
