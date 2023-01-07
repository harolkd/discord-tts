import shutil, os, json
import uberduckapi as ub
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()

config = json.load(open('config.json'))
language = json.load(open(f'./langs/{config["language"]}.json'))

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

    for server in bot.guilds:
        os.mkdir(f"files/{server.id}")

    for server in bot.guilds:
        txt = open(f'files/{server.id}/data.txt', 'w+')
        txt.write("Nobody")
        txt.close()
    return

async def googleTTS(message, x, server):
    speech = gTTS(text = message, lang = x, slow = False)
    speech.save(f"./files/{server}/audio.mp3")

#requires token
def uberduckTTS(message, voice, server):
    duck = ub.UberDuck(os.getenv('U_KEY'), os.getenv('U_SECRET'))
    sponge = duck.get_voice(voice, message)

    if sponge:
        return sponge.save(f'./files/{server}/audio.mp3')
    else:
        return language["uberduck"]["error1"]

#requires token
def msTTS(message):
    return

def pyTTSx3(message):
    return