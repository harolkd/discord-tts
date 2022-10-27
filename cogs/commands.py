import discord, time
from discord.ext import commands

def updateI(self, ctx):
    channel = ctx.guild.me.voice.channel
    i = self.bot.get_channel(channel.id).members
    return print(len(i))

class Commander(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        if(ctx.author.voice):
            channel = ctx.author.voice.channel
            if channel == ctx.voice_client:
                pass
            elif ctx.voice_client is None:
                await channel.connect()
            else:
                await ctx.voice_client.move_to(channel)
            return
        else:
            return await ctx.send("Debes estar en un canal")

    @commands.command()
    async def leave(self, ctx):
        channel = ctx.author.voice.channel
        if channel != None:
            try:
                await ctx.voice_client.disconnect()
            except:
                pass
        else:
            ctx.send("Tienes que estar en un canal de voz")
        return

    @commands.command()
    async def foo(self, ctx):
        server = ctx.guild.id
        channel = ctx.guild.me.voice.channel
        members = self.bot.get_channel(channel.id).members
        voice_channel = ctx.guild.me.voice.channel
        print(channel.id)
        return

async def setup(bot):
    await bot.add_cog(Commander(bot))
