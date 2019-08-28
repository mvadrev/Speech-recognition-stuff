import librosa
from librosa import display
import os
import torch
import torch.nn as nn
import numpy as np
import pylab

save_path = 'b3.jpg'

data,sr = librosa.load('b (3).WAV',44100)


pylab.axis('off') # no axis
pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
stft = librosa.stft(data)
Xdb = librosa.amplitude_to_db(abs(stft))
librosa.display.specshow(Xdb, sr=44100, x_axis='time', y_axis='time')
pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
#pylab.close()

