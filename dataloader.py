import os
import librosa
from librosa import display
import pylab
import numpy as np

full_path = '..\librosa\library'
file_list = os.listdir(full_path)


path_sub = []
fin_list = []
file_list_only = []

for dir in file_list:
   temp = os.path.join(full_path,dir)
   path_sub.append(temp)

suffix = '.wav'
for files in path_sub:
   if os.path.isdir(files):
       files_sub_temp = os.listdir(files)
       
       for lists in files_sub_temp:
           if lists.endswith(suffix):
               fin_temp = os.path.join (str(files),str(lists))
               fin_list.append(fin_temp)
               file_list_only.append(lists)

                
data_list = []
file_count = 0

for i in fin_list:
    data,sr = librosa.load(i,44100)
    stft = librosa.stft(data)
    Xdb = librosa.amplitude_to_db(abs(stft))
    librosa.display.specshow(Xdb, sr=44100, x_axis='time', y_axis='log')
    #pylab.savefig('file'+str(file_count)+'.jpg', bbox_inches=None, pad_inches=0)
    pylab.savefig(file_list_only[file_count].split('.')[0]+'.jpg', bbox_inches=None, pad_inches=0)
    file_count +=1

