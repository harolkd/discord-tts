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
                await ctx.voice_client.disconnect()
            except:
                pass
        else:
            ctx.send("Tienes que estar en un canal de voz")

    @commands.command()
    async def foo(self, ctx):
        server = ctx.guild.id
        channel = ctx.guild.me.voice.channel
        members = self.bot.get_channel(channel.id).members

        #while True:
        #    i = self.bot.get_channel(channel.id).members
        #    if len(i) < 2:
        #        await ctx.voice_client.disconnect()
        #        break
        #    print("sleep")
        return

async def setup(bot):
    await bot.add_cog(Commander(bot))
