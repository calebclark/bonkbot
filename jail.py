import discord
import config
class Jail:

    cf = config.get_instance()    

    # Initialized with the jail
    def __init__(self, guild):
        for channel in guild.channels:
            if channel.name == self.cf.get("jail_name") and isinstance(channel, discord.VoiceChannel):
                self.jail = channel
                return

    def has_jail(self):
        if self.jail is None:
            return False
        return True

    # True if the given member is not in jail and is in voice.
    def can_jail(self, member):
        if member.bot:
            return False
        if not self.has_jail():
            return False
        voice = member.voice
        if voice is None or voice.channel is None or voice.channel == self.jail:
            return False
        return True


    # Move the given member to jail if they are in voice, returns true if the member was jailed, false otherwise
    async def add(self, member):
        if self.can_jail(member):
            await member.edit(voice_channel = self.jail)
            print("added " + member.name + " to jail")
            return True
        print("failed to add " + member.name + " to jail")
        return False
