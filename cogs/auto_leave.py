import discord, time, os
from main import config
from discord.ext import commands

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        #time.sleep(15)
        
        for folder in os.listdir("./files"):
            if os.path.exists("files/{folder}/channel.txt"):
                txt = open('files/{folder}/channel.txt', 'r')
                beautyID = int(txt.read())
                txt.close()

                channel = self.bot.get_channel(beautyID)
                if len(channel.members) < 2:
                    try:
                        await discord.utils.get(self.bot.voice_clients).disconnect()
                    except:
                        pass
        return

        

async def setup(bot):
    await bot.add_cog(Voice(bot))
