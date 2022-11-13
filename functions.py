import shutil, os
import uberduckapi as ub
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()

def checkData(message, author, server):
    txt = open(f'files/{server}/data.txt', 'r+')
    if ("()" in message) or (author == txt.read()):
        txt = open(f'files/{server}/data.txt', 'w')
        txt.write("()")
    else:
        txt = open(f'files/{server}/data.txt', 'w')
        txt.write(author)
    txt.close()
    return

def setupFiles(bot):
    #Clean Remaning Data
    if os.path.exists("files") == True:
        shutil.rmtree("files")
    #Create new server files
    os.mkdir("files")

    for guild in bot.guilds:
        os.mkdir(f"files/{guild.id}")

    for guild in bot.guilds:
        txt = open(f'files/{guild.id}/data.txt', 'w+')
        txt.write("Nobody")
        txt.close()
    return

async def googleTTS(message, x, guild):
    speech = gTTS(text = message, lang = x, slow = False)
    speech.save(f"./files/{guild}/audio.mp3")

#requires token
def uberduckTTS(message, voice):
    duck = ub.UberDuck(os.getenv('KEY'), os.getenv('SECRET'))
    sponge = duck.get_voice(voice, message)

    if sponge:
        return sponge.save('./files/audio.mp3')

#requires token
def msTTS(message):
    return

def pyTTSx3(message):
    return
