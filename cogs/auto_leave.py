import discord
from os import path
from main import config
from discord.ext import commands

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if path.exists("files/channel.txt"):
            txt = open('files/channel.txt', 'r')
            beautyID = int(txt.read())
            txt.close()

            channel = self.bot.get_channel(beautyID)
            if len(channel.members) < 2:
                print("TRUEEE")
                for  i in self.bot.voice_clients:
                    await i.disconnect()
            else:
                pass
        return

async def setup(bot):
    await bot.add_cog(Voice(bot))