import simpleaudio as sa
import numpy as np

def speak_response(state):
    text = state["response"]
    audio = tts.tts(text)
    if not isinstance(audio, np.ndarray):
        audio = audio[0]
    
    # Convert float32 audio [-1.0, 1.0] to 16-bit PCM
    audio_int16 = np.int16(audio * 32767)
    
    play_obj = sa.play_buffer(audio_int16, 1, 2, 22050)
    play_obj.wait_done()
    return state
