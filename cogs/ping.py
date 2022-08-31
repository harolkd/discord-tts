import discord
from discord.ext import commands

class Commander(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("PONG AND PONG!!")
        
async def setup(bot):
    await bot.add_cog(Commander(bot))
