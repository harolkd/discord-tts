import shutil, os

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