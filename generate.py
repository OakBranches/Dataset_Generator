import os
from PIL import Image
from random import randrange


def cleanDir(directory):
    for file in os.listdir(directory):
        filepath = directory + file
        os.remove(filepath)



def insertDiego(filepath):
    back = Image.open(filepath)
    back_im = back.copy()

    d_directory = "./Origin/Diego/"
    d_files = os.listdir(d_directory)
    d_file = d_files[randrange(len(d_files))]
    d_filepath = d_directory + d_file

    angle = randrange(0,360)
    d = Image.open(d_filepath).rotate(angle)
    factor = 1/randrange(4,16)
    diego = d.resize((round(back.size[0]*factor), round(back.size[1]*factor)))
    position = (randrange(back.size[0]-diego.size[0]), randrange(back.size[1]-diego.size[1]))
    back_im.paste(diego, position)
    return back_im

cleanDir("./Output/No/")
cleanDir("./Output/Yes/")

a_directory = "./Origin/Photos/"
for filename in os.listdir(a_directory):
    filepath = os.path.join(a_directory, filename)
    i = randrange(1,100)
    filename = filename.split(".")[0]+'.png'
    if i > 50:
        img = insertDiego(filepath)
        img.save(f'./Output/Yes/{filename}')
    else:
        img = Image.open(filepath)
        img.save(f'./Output/No/{filename}')







