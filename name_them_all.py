from PIL import Image
import pytesseract as pyt
from os import listdir,rename
from os.path import isfile, join
import os

mypath='' #e.g. mypath='/home/igor/Dokumenty/MemeReader'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def renamememe(memename):
    os.rename(mypath+'/'+memename,mypath+'/'+readmeme(memename)[:255:])

def readmeme(memename):
    path=mypath+'/'+memename
    meme=Image.open(path)
    text=pyt.image_to_string(path)
    meme.close()
    text=text.replace('\n', ' ')
    return text

def dzialaj():
    for i in range(len(files)):
        if(files[i][-5::]=='.jpeg' or files[i][-4::]=='.jpg' or files[i][-4::]=='.png'):
            renamememe(files[i])

dzialaj()