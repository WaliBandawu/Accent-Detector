import os
import subprocess
import requests
from urllib.parse import urlparse

def download_video(url: str, output_path: str) -> bool:
    """
    Downloads a video from a direct URL to output_path.
    Only supports direct links (e.g., .mp4).
    Returns True if successful, else False.
    """
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        return True

    except Exception as e:
        print(f"[ERROR] Video download failed: {e}")
        return False


def extract_audio(video_path: str, audio_path: str) -> bool:
    """
    Extracts mono 16kHz WAV audio from video using ffmpeg.
    Returns True if successful, else False.
    """
    try:
        cmd = [
            "ffmpeg",
            "-y",          # Overwrite output
            "-i", video_path,
            "-ac", "1",    # Mono audio
            "-ar", "16000",# Sample rate 16kHz
            "-vn",         # Disable video
            audio_path
        ]

        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return True

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Audio extraction failed: {e.stderr.decode()}")
        return False


def download_and_extract_audio(video_url: str, audio_path: str) -> bool:
    """
    Downloads a video from a URL and extracts audio as 16kHz mono WAV.
    Returns True if both steps succeed, else False.
    """
    os.makedirs("tmp", exist_ok=True)
    tmp_video_path = "tmp/tmp_video.mp4"

    try:
        if not download_video(video_url, tmp_video_path):
            return False

        if not extract_audio(tmp_video_path, audio_path):
            return False

        return True

    finally:
        # Cleanup even on failure
        if os.path.exists(tmp_video_path):
            os.remove(tmp_video_path)
