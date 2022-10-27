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
        author = ctx.author.name
        server = ctx.guild.id
        #check if bot is talking
        if (ctx.voice_client is not None) and (ctx.voice_client.is_playing()):
            return await ctx.send("Espera a que termine de hablar")

        txt = open('files/data.txt', 'r+')
        data = txt.read()
        txt.close

        if data == "Nobody":
            checkData(arg, author, server)
        elif data == author:
            author = "()"
            if "()" in arg:
                checkData(arg, author, server)
        elif data != author:
            checkData(arg, author, server)

        #anonimous message
        if ("()" not in arg) or ("()" in author):
            arg = "%s dice. %s" % (author, arg)

        if "@" in arg:
            return await ctx.send("No me hagas mencionar a usuarios, por favor")

        speech = gTTS(text = arg, lang = config['language'], slow = False)
        speech.save("./files/audio.mp3")

        await ctx.invoke(self.bot.get_command('join'))
        return ctx.voice_client.play(FFmpegPCMAudio("./files/audio.mp3"))

async def setup(bot):
    await bot.add_cog(Speaker(bot))
