import pyaudio
import numpy as np
import time

FRAMES_PER_BUFFER = 3200 # number of frames per buffer 
FORMAT = pyaudio.paInt16 # 16-bit integer format
CHANNELS = 1 # single channel
RATE = 16000 # 16 kHz sampling rate, 16,000 samples per second. Higher sampling rate means better quality. However, it also means more data to process.
p = pyaudio.PyAudio()

def record_audio():
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER,
    )

    print("start recording...") 

    frames = []
    seconds = 1
    for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)

    print("recording stopped")

    stream.stop_stream()
    stream.close()
    
    return np.frombuffer(b''.join(frames), dtype=np.int16)


def terminate():
    p.terminate()
