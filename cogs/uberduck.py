import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from functions import uberduckTTS
from main import config

class Uberduck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uberduck(self, ctx, arg1, arg2):
        server = ctx.guild.id
        #check if bot is talking
        if (ctx.voice_client is not None) and (ctx.voice_client.is_playing()):
            return await ctx.send("Espera a que termine de hablar")

        if "@" in arg2:
            return await ctx.send("No me hagas mencionar a usuarios, por favor")
        
        print("Checks done")
        uberduckTTS(arg2, arg1, server) #rick-sanchez
        print("Uberduck file")
        await ctx.invoke(self.bot.get_command('join'))
        print("Playing audio")
        return ctx.voice_client.play(FFmpegPCMAudio(f"./files/{server}/audio.mp3"))

async def setup(bot):
    await bot.add_cog(Uberduck(bot))
