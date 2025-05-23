import os
import torchaudio
from transformers import pipeline

# Initialize the Hugging Face pipeline for accent detection
pipe = pipeline("audio-classification", model="HamzaSidhu786/speech-accent-detection")

def preprocess_audio(audio_path: str, target_sr: int = 16000) -> str:
    """
    Preprocess the audio: resample to 16kHz mono and save as temporary file.
    """
    signal, sr = torchaudio.load(audio_path)

    # Resample if necessary
    if sr != target_sr:
        resampler = torchaudio.transforms.Resample(orig_freq=sr, new_freq=target_sr)
        signal = resampler(signal)

    # Convert to mono if stereo
    if signal.shape[0] > 1:
        signal = signal.mean(dim=0, keepdim=True)

    tmp_path = "tmp_audio.wav"
    torchaudio.save(tmp_path, signal, target_sr)
    return tmp_path

def classify_accent(audio_path: str) -> dict:
    """
    Classifies the English accent in an audio file.
    """
    tmp_path = None
    try:
        tmp_path = preprocess_audio(audio_path)

        results = pipe(tmp_path)
        top_result = results[0]

        return {
            "accent": top_result["label"],
            "score": round(top_result["score"], 3),
            "summary": f"The model detected a {top_result['label']} accent with confidence {round(top_result['score'] * 100, 1)}%"
        }

    except Exception as e:
        return {"error": f"Failed to classify accent: {str(e)}"}

    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)


