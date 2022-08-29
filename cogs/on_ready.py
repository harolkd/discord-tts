import discord
from discord.ext import commands

class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     
    @commands.Cog.listener() 
    async def on_ready(self):
        #await self.bot.change_presence(activity = discord.Streaming(name = "Nuestra Señora de Paris", url = "https://www.twitch.tv/robtop"))
        return print(f'O')
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("PONG AND PONG!!")
        
async def setup(bot):
    await bot.add_cog(Start(bot))
