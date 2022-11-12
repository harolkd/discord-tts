import shutil, os
import uberduckapi as ub
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()

def checkData(message, autor, server):
    txt = open('files/data.txt', 'w')
    if "()" in message:
        txt.write(autor + "()")
    else:
        txt.write(autor)     
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
        print(f"ready {guild}")

    for guild in bot.guilds:
        print(f"{guild.id}")
        txt = open(f'files/{guild.id}/data.txt', 'w+')
        txt.write("Nobody")
        txt.close()
    return

def googleTTS(message, x):
    speech = gTTS(text = message, lang = x, slow = False)
    speech.save("./files/audio.mp3")

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
