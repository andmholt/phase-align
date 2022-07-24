import wave
import numpy as np
import matplotlib.pyplot as plt

from align import align

f1sig = None
f2sig = None

with wave.open('../OH 1.03_03.wav') as f1:
    f1framerate = f1.getframerate()
    f1frames = f1.getnframes()
    f1channels = f1.getnchannels()
    f1width = f1.getsampwidth()
    f1params = f1.getparams()
    print('sampling rate:', f1framerate, 'Hz')
    print('length:', f1frames, 'samples')
    print('channels:', f1channels)
    print('sample width:', f1width, 'bytes')
    
    f1data = f1.readframes(f1frames)
    
    f1sig = np.frombuffer(f1data, dtype='<i2').reshape(-1, f1channels)
    print(f1sig)
    
with wave.open('../OH 2.03_03.wav') as f2:
    f2framerate = f2.getframerate()
    f2frames = f2.getnframes()
    f2channels = f2.getnchannels()
    f2width = f2.getsampwidth()
    f2params = f2.getparams()
    print('sampling rate:', f2framerate, 'Hz')
    print('length:', f2frames, 'samples')
    print('channels:', f2channels)
    print('sample width:', f2width, 'bytes')
    
    f2data = f2.readframes(f2frames)
    
    f2sig = np.frombuffer(f2data, dtype='<i2').reshape(-1, f2channels)
    #print(f2sig)

f2aligned = align(f1sig, f2sig)
f2ravel = np.ravel(f2aligned, order='A')
f2bytes = f2ravel.tobytes()

#print(f2data[:10])
#print(np.frombuffer(f2data, dtype='<i2')[:10])
#print(np.frombuffer(f2data, dtype='<i2').reshape(-1, f2channels))
#f2ravel = np.ravel(f2sig, order='A')
#print(f2ravel[:10])
#print(f2ravel.tobytes()[:10])

with wave.open('../OH 2_aligned.wav', mode='wb') as f2a:
    f2a.setparams(f2params)
    f2a.writeframes(f2bytes)