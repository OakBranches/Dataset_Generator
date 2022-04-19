import os
from PIL import Image

def search(dir, to,prefix = ""):
    for filename in os.listdir(dir):
        filepath = os.path.join(dir, filename)
        try:
            search(filepath, to ,f'{prefix}_{filename}')
        except:        
            try:
                d = Image.open(filepath)
                filename = filename.split('.')[0] + '.png'
                d.save(f'{to}{prefix+filename}')
            except Exception as e:
                print(e)
                pass

a_directory = "./Origin/Photos/"

search('./teste/', a_directory ,"")