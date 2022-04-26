import os
from PIL import Image
from random import randrange, randint




def cleanDir(directory):
    for file in os.listdir(directory):
        filepath = directory + file
        os.remove(filepath)



def insertDiego(filepath):
    back = Image.open(filepath).resize((200,200))
    back_im = back.copy().convert('RGB')

    d_directory = "./Origin/Diego/"
    d_files = os.listdir(d_directory)
    d_file = d_files[randrange(len(d_files))]
    d_filepath = d_directory + d_file

    angle = randint(0,360)
    d = Image.open(d_filepath)
    factor = 1/randint(1,10)
    diego = d.resize((round(back.size[0]*factor), round(back.size[1]*factor))).convert('RGBA')
    position = (randint(0,back.size[0]-diego.size[0]), randint(0,back.size[1]-diego.size[1]))
    diego = diego.rotate(angle, expand=True)
    back_im.paste(diego, position, diego)

    return back_im

dirs = ['train', 'test', 'valid']
for i in dirs: 
    os.makedirs(f'./Output/{i}/Yes', exist_ok=True)
    os.makedirs(f'./Output/{i}/No', exist_ok=True)
    cleanDir(f'./Output/{i}/No/')
    cleanDir(f'./Output/{i}/Yes/')

a_directory = "./Origin/Photos/"
for filename in os.listdir(a_directory):
    try:
        filepath = os.path.join(a_directory, filename)
        i = randrange(1,100)
        j = randrange(1,100)
        filename = filename.split(".")[0]+'.png'
        
        prefix = "train" if j < 70 else "valid" if j < 80 else "test"
        if i > 50:
            img = insertDiego(filepath)
            img.save(f'./Output/{prefix}/Yes/{filename}')
        else:
            img = Image.open(filepath).resize((200,200))
            img.save(f'./Output/{prefix}/No/{filename}')
    except:
        pass







