import discord
from main import config
from discord.ext import commands

class Starter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = {}
     
    @commands.Cog.listener() 
    async def on_ready(self):
        self.vc[id] = None
        activity = discord.Streaming(name=config['activity_name'], url=config['url'])
        await self.bot.change_presence(activity=activity)
        return print(f'Bot is running')
        
async def setup(bot):
    await bot.add_cog(Starter(bot))
