# nodes/whisper_transcribe.py
import whisper
import tempfile
import soundfile as sf

model = whisper.load_model("base")  # or "medium", "large" as needed

def transcribe_audio(state):
    audio_data = state["audio"]
    
    # Save raw audio to a temp file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        sf.write(tmp.name, audio_data, 16000, format="WAV")  # Assuming 16kHz mono
        result = model.transcribe(tmp.name)
    
    return {"transcript": result["text"]}
