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

def setupFiles():
    #Clean Remaning Data
    if os.path.exists("files") == True:
        shutil.rmtree("files")
    #Create new server files    
    os.mkdir("files")
    txt = open('files/data.txt', 'w')
    txt.write("Nobody")
    txt.close()

def googleTTS(message, len):
    speech = gTTS(text = arg, lang = len, slow = False)
    speech.save("./files/audio.mp3")

def uberduck(message, voice):
    duck = ub.UberDuck(os.getenv('KEY'), os.getenv('SECRET'))
    sponge = duck.get_voice(voice, message)

    if sponge:
        return sponge.save('./files/audio.mp3')

#requires token
def msTTS(message):
    return

def pyTTSx3(message):
    return