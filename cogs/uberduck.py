import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from functions import uberduckTTS
from main import config

class Uberduck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uberduck(self, ctx, arg1, *, message):
        server = ctx.guild.id
        #check if bot is talking
        if (ctx.voice_client is not None) and (ctx.voice_client.is_playing()):
            return await ctx.send(f'{language["say"]["error1"]}')

        if "@" in message:
            return await ctx.send(f'{language["say"]["error2"]}')

        uberduckTTS(message, arg1, server) #rick-sanchez
        await ctx.invoke(self.bot.get_command('join'))
        return ctx.voice_client.play(FFmpegPCMAudio(f"./files/{server}/audio.mp3"))

async def setup(bot):
    await bot.add_cog(Uberduck(bot))
