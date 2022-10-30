import shutil, os, uberduck
from gtts import gTTS
from dotenv import load_dotenv
from io import StringIO, BytesIO

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

def uberduck(message):
    client = uberduck.UberDuck(os.getenv('KEY'), os.getenv('SECRET'))
    voices = uberduck.get_voices(return_only_names = True)

    speech = input('Enter speech: ')
    voice = input('Enter voice or enter "LIST" to see list of voices: ')

    if voice == 'LIST':
        print('Available voices:\n')
        for voice in sorted(voices): # sorting the voice list in alphabetical order
            print(voice)
        exit()

    if voice not in voices:
        print('Invalid voice')
        exit()

    result = client.speak(speech, voice, check_every = 0.5)
    return print(BytesIO(result))

#requires token
def msTTS(message):
    return

def pyTTSx3(message):
    return