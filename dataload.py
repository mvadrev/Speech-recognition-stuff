import os

parentdir = '..\librosa'
sounds = 'library'



sound_folder = os.listdir(os.path.join(parentdir,sounds))

list = []
folders_dir = os.path.join(parentdir, sounds)

for i in sound_folder:
    
    if os.path.isdir(os.path.join(parentdir, sounds)):
        list.append(str(i))
        
for dir in list:
    
    try:
    
        #print(folders_dir,dir,os.listdir(os.path.join(parentdir,sounds,dir)))
        print(os.listdir(os.path.join(parentdir,sounds,dir)))
    except NotADirectoryError:
            pass
        


    

