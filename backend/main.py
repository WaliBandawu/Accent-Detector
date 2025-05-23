from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from inference import classify_accent
from utils.media_utils import download_and_extract_audio
import uuid
import os

app = FastAPI(title="Accent Classification API")

class VideoInput(BaseModel):
    video_url: str

@app.post("/analyze/")
def analyze_accent(data: VideoInput):
    session_id = str(uuid.uuid4())
    audio_path = f"tmp/{session_id}.wav"
    os.makedirs("tmp", exist_ok=True)

    try:
        # Step 1: Download and extract audio
        success = download_and_extract_audio(data.video_url, audio_path)
        if not success:
            raise HTTPException(status_code=400, detail="Audio extraction failed.")

        # Step 2: Run accent classification
        result = classify_accent(audio_path)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

    finally:
        # Step 3: Cleanup
        if os.path.exists(audio_path):
            os.remove(audio_path)
