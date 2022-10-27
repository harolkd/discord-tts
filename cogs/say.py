import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from functions import checkData
from gtts import gTTS
from main import config

class Speaker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, arg):
        autor = ctx.author.name
        server = ctx.guild.id
        #check if bot is talking
        if (ctx.voice_client is not None) and (ctx.voice_client.is_playing()):
            return await ctx.send("Espera a que termine de hablar")

        txt = open('files/data.txt', 'r+')
        data = txt.read()
        txt.close

        if data == "Nobody":
            checkData(arg, autor, server)
        elif data == autor:
            autor = "()"
            if "()" in arg:
                checkData(arg, autor, server)
        elif data != autor:
            checkData(arg, autor, server)

        #anonimous message
        if ("()" not in arg) or ("()" in autor):
            arg = "%s dice. %s" % (autor, arg)

        if "@" in arg:
            return await ctx.send("No me hagas mencionar a usuarios, por favor")

        speech = gTTS(text = arg, lang = config['language'], slow = False)
        speech.save("./files/audio.mp3")

        if(ctx.author.voice):
            channel = ctx.author.voice.channel
            #condiciones
            if channel == ctx.voice_client:
                pass
            elif ctx.voice_client is None:
                await channel.connect()
            else:
                await ctx.voice_client.move_to(channel)

            return ctx.voice_client.play(FFmpegPCMAudio("./files/audio.mp3"))
        else:
            return await ctx.send("Debes estar en un canal")

async def setup(bot):
    await bot.add_cog(Speaker(bot))
