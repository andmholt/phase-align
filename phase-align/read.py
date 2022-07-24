import wave
import numpy as np

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
    
    f1sig = np.frombuffer(f1data, dtype='<i2').reshape(-1, f1channels)

    print(f1sig)