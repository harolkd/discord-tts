import discord, os, shutil, json
from discord.ext import commands
from discord import FFmpegPCMAudio
from gtts import gTTS
from dotenv import load_dotenv
from functions import setupFiles, checkData

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

config = json.load(open('config.json'))

bot = commands.Bot(command_prefix=config['prefix'], description=config['description'], intents=intents)

@bot.event
async def on_ready():
    activity = discord.Streaming(name=config['activity_name'], url=config['url'])
    await bot.change_presence(activity=activity)
    print(f'{bot.user} O')

@bot.command()
async def ping(ctx, message):
    await ctx.send("PONG!!")

@bot.command()
async def say(ctx, *, message):
    autor = ctx.message.author.name
    server = ctx.message.guild.id
    #check if bot is talking
    if ctx.voice_client is None:
        pass
    else:
        if (ctx.voice_client.is_playing()):
            await ctx.send("espera a que termine de hablar")

    if "@" in message:
        await ctx.send("No me hagas mencionar a usuarios, por favor")
        return

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
    if "@" in message:
        await ctx.send("No me hagas mencionar a usuarios, por favor")

    if ("()" in message) or ("()" in autor):
        pass
    else:
        message = "%s dice. %s" % (autor, message)

    speech = gTTS(text = message, lang = "es", slow = False)
    speech.save("./files/audio.mp3")
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
        ctx.voice_client.play(FFmpegPCMAudio("./files/audio.mp3"))
    else:
        await ctx.send("Debes estar en un canal")

@bot.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.author.voice.channel
        #conditions to make possible connect.
        if(channel == ctx.voice_client):
            pass
        elif(ctx.voice_client is None):
            await channel.connect()
        else:
            await ctx.voice_client.move_to(channel)
    else:
        await ctx.send("Debes estar en un canal de voz")

@bot.command(pass_context = True)
async def leave(ctx):
    if(ctx.author.voice):
        channel = ctx.author.voice.channel
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("Debes estar en un canal de voz")

setupFiles()
bot.run(os.getenv('TOKEN'))
