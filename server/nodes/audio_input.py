# nodes/audio_input.py
import pyaudio
import numpy as np

def capture_audio(state):
    duration = 5  # seconds
    rate = 16000  # Whisper prefers 16 kHz
    chunk = 1024
    channels = 1
    format = pyaudio.paInt16

    p = pyaudio.PyAudio()
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("🎙️ Recording... Speak now!")
    frames = []

    for _ in range(int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(np.frombuffer(data, dtype=np.int16))

    print("🛑 Done recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Combine chunks and normalize
    audio_np = np.concatenate(frames).astype(np.float32) / 32768.0  # normalize to [-1, 1]
    
    return {"audio": audio_np}
