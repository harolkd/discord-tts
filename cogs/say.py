import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from functions import checkData, googleTTS, language
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
            return await ctx.send(f'{language["say"]["error1"]}')

        await ctx.invoke(self.bot.get_command('join'))
        #check data.txt
        checkData(message, author, server)

        txt = open(f'files/{server}/data.txt', 'r+')
        author = txt.read()
        txt.close()

        #anonimous message
        if author == "()":
            pass
        else:
            message = "%s dice. %s" % (author, message)

        if "@" in message:
            return await ctx.send(f'{language["say"]["error2"]}')

        await googleTTS(message, config['language'], server)
        return ctx.voice_client.play(FFmpegPCMAudio(f"./files/{server}/audio.mp3"))

async def setup(bot):
    await bot.add_cog(Speaker(bot))
