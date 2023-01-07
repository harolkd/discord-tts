import discord
from main import config
from discord.ext import commands

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        print(f"{len(after.channel)} AFTER")
        #print(f"{before.channel} BEFORE")
        #if before.channel.id == "862450695419461672":
        #    if len(before.channel.members) == 1:
        #        await ctx.invoke(self.bot.get_command('leave'))

async def setup(bot):
    await bot.add_cog(Voice(bot))
