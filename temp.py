import librosa
X, sample_rate, = librosa.load('mc.wav')
import numpy as np

win_length =   20000         #int(0.080 * sample_rate) =551
hop_length =  int(win_length // 4)
#ahop_length = 512
mfccs = librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40, n_fft=win_length, hop_length=hop_length)
librosa.display.waveplot(X, sr=20000)

import matplotlib.pyplot as plt
import librosa.display
librosa.display.specshow(X, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()

rms = librosa.feature.rms(X)

plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(rms.T, label='RMS Energy')
plt.xticks([])
plt.xlim([0, rms.shape[-1]])
plt.legend()
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(X, ref=np.max),y_axis='log', x_axis='time')
plt.title('log Power spectrogram')
plt.tight_layout()