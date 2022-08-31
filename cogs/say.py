import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from functions import checkData
from gtts import gTTS

class Commander(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     
    @commands.command()
    async def say(ctx, message):
        autor = ctx.message.author.name
        #check if bot is talking
        if ctx.voice_client is None:
            pass
        else:
            if (ctx.voice_client.is_playing()):
                await ctx.send("espera a que termine de hablar")
    
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
    
        if message == None:
            message = "Hola, me llamo super alexia"
    
        #anonimous message
        if ("()" in message) or ("()" in autor):
            pass
        else:
            message = "%s dice. %s" % (autor, message)
        #new message
        print(message)
        #brasilian voice
        if "ç" in message:
            speech = gTTS(text = message, lang = "pt", slow = False)
        else:
            speech = gTTS(text = message, lang = "es", slow = False)
        #create audio
        speech.save("./files/audio.mp3")
        print("created file")
        #check voice channel
        if(ctx.author.voice):
            channel = ctx.author.voice.channel
            #condiciones
            if channel == ctx.voice_client:
                pass
            elif ctx.voice_client is None:
                await channel.connect()
            else:
                await ctx.voice_client.move_to(channel)
            #voice = await channel.connect()
            if "@" in message:
                await ctx.send("No me hagas mencionar a usuarios, por favor")
            else:
                ctx.voice_client.play(FFmpegPCMAudio("./files/audio.mp3"))
                print("playing audio")
        else:
            await ctx.send("Debes estar en un canal")
        
async def setup(bot):
    await bot.add_cog(Commander(bot))
