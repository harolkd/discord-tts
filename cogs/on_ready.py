import discord
from main import config
from discord.ext import commands
from functions import setupFiles, language

class Starter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Streaming(name=config['activity_name'], url=config['url'])
        await self.bot.change_presence(activity=activity)
        print(f'{language["on_ready"]}')

        return setupFiles(self.bot)

async def setup(bot):
    await bot.add_cog(Starter(bot))
