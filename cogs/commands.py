import discord, time
from discord.ext import commands

class Commander(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = {}

    @commands.command()
    async def join_VC(self, ctx, channel):
        id = int(ctx.guild.id)
        if self.vc[id] == None or not self.vc[id].is_connected():
            self.vc[id] = await channel.connect()
            if self.vc[id] == None:
                ctx.send("Lo siento, error problemático")
                return
        else:
            self.vc[id].move_to(channel)

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        if ctx.author.voice:
            try:
                await self.join_VC(ctx, channel)
            except:
                pass
        else:
            ctx.send("Tienes que estar en un canal de voz")

    @commands.command()
    async def leave(self, ctx):
        channel = ctx.author.voice.channel
        if channel != None:
            try:
                await self.disconnect()
            except:
                pass
        else:
            ctx.send("Tienes que estar en un canal de voz")

    @commands.command()
    async def foo(self, ctx):
        channel = ctx.guild.me.voice.channel
        members = self.bot.get_channel(channel.id).members
        voice_client = ctx.guild.voice_client

        while True:
            time.sleep(3)
            members = self.bot.get_channel(channel.id).members
            if len(members) < 5:
                await voice_client.disconnect()

async def setup(bot):
    await bot.add_cog(Commander(bot))
