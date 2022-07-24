import wave
import numpy as np

from align import align

data = None

with wave.open('../f1.wav') as f1:
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
    data = f1data
    
    f1sig = np.frombuffer(f1data, dtype='<i2').reshape(-1, f1channels)

f1ravel = np.ravel(f1sig, order='A')
f1bytes = f1ravel.tobytes()

with wave.open('../f1_back.wav', mode='wb') as f1a:
    f1a.setparams(f1params)
    f1a.writeframes(f1bytes)