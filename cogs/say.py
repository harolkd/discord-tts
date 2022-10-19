import discord, json
from discord.ext import commands
from discord import FFmpegPCMAudio
from functions import checkData
from gtts import gTTS
config = json.load(open('config.json'))

class Speaker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(ctx, arg):
        autor = ctx.message.author.name
        message = arg
        if message == None:
            message = "Hola, me llamo super alexia"
        #check if bot is talking
        if (ctx.voice_client is not None) and (ctx.voice_client.is_playing()):
            return await ctx.send("Espera a que termine de hablar")

        txt = open('files/data.txt', 'r+')
        data = txt.read()
        txt.close

        if data == "Nobody":
            checkData(message, autor, server)
        elif data == autor:
            autor = "()"
            if "()" in message:
                checkData(message, autor, server)
        elif data != autor:
            checkData(message, autor, server)

        #anonimous message
        if ("()" not in message) or ("()" in autor):
            message = "%s dice. %s" % (autor, message)

        if "@" in message:
            return await ctx.send("No me hagas mencionar a usuarios, por favor")

        speech = gTTS(text = message, lang = config['language'], slow = False)
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
