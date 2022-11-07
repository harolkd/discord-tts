import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from functions import checkData, googleTTS
from main import config

class Speaker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, message):
        author = ctx.author.name
        server = ctx.guild.id
        #check if bot is talking
        if (ctx.voice_client is not None) and (ctx.voice_client.is_playing()):
            return await ctx.send("Espera a que termine de hablar")

        txt = open('files/data.txt', 'r+')
        data = txt.read()
        txt.close

        if data == "Nobody":
            checkData(message, author, server)
        elif data == author:
            author = "()"
            if "()" in message:
                checkData(message, author, server)
        elif data != author:
            checkData(message, author, server)

        #anonimous message
        if ("()" not in message) or ("()" in author):
            message = "%s dice. %s" % (author, message)

        if "@" in message:
            return await ctx.send("No me hagas mencionar a usuarios, por favor")
        print(message)

        googleTTS(message, config['language'])
        await ctx.invoke(self.bot.get_command('join'))
        return ctx.voice_client.play(FFmpegPCMAudio("./files/audio.mp3"))

async def setup(bot):
    await bot.add_cog(Speaker(bot))
