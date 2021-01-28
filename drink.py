#!/usr/bin/env python3
import discord
import config
import util

class Drink:
    cf = config.get_instance()    
    drink_map = {"shot": 1, "shots": 1, "drink" : 1, "ipa" : 2}

    async def message_handler(self, message, jail, bonkbot):
        author = message.author
        msg = util.sanitize(message.content)
        if msg == "reset":
            counts = self.cf.get("counts")
            counts[message.author.name] = 0
            self.cf.put("counts", counts)
            await util.send_message(message.channel, message.author.name + "'s drink count is " + str(counts[message.author.name]))
            await message.delete(delay = 60)
        if msg in self.drink_map:
            counts = self.cf.get("counts")
            print(counts)
            if message.author.name in counts:
                print("in map")
                counts[message.author.name] += self.drink_map[msg]
            else:
                print("not in map")
                counts[message.author.name] = 1
            print(counts)
            self.cf.put("counts", counts)
            await util.send_message(message.channel, message.author.name + "'s drink count is " + str(counts[message.author.name]))
            await message.delete(delay = 60)
            return
        if msg == "scoreboard":
            output = ""
            for person, count in sorted(self.cf.get("counts").items(), key=lambda kv: -kv[1]):
                output += str(count) + " | " + person + "\n"
            await message.channel.send(output)
            await message.delete(delay = 60)
