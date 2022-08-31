import discord
from discord.ext import commands

class Starter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     
    @commands.Cog.listener() 
    async def on_ready(self):
        await self.bot.change_presence(activity = discord.Streaming(name = "Nuestra Señora de Paris", url = "https://www.twitch.tv"))
        return print(f'Bot is running')
        
async def setup(bot):
    await bot.add_cog(Starter(bot))
