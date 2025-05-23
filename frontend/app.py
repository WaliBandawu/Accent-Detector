import streamlit as st
import requests
import logging

# --- Configure Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="streamlit_app.log",  # Log file name
    filemode="a"
)

API_URL = "http://localhost:8000/analyze/"  # Update if deployed elsewhere

st.set_page_config(page_title="English Accent Classifier", layout="centered")

st.title("🎙️ English Accent Classifier")
st.write("Paste a public video URL (e.g., Loom or MP4). We'll extract the audio, analyze it, and return the predicted English accent.")

video_url = st.text_input("🔗 Video URL")

if st.button("Analyze") and video_url:
    logging.info(f"Analyze button clicked with URL: {video_url}")
    with st.spinner("Analyzing... Please wait."):
        try:
            response = requests.post(API_URL, json={"video_url": video_url})
            logging.info(f"POST to {API_URL} returned status code {response.status_code}")
            data = response.json()

            if response.status_code == 200:
                st.success("✅ Accent Analysis Complete!")
                st.markdown(f"**Accent:** `{data['accent']}`")
                st.markdown(f"**Confidence Score:** `{int(data['score']*100)}%`")
                st.info(data.get("summary", "No summary available."))
                logging.info(f"Prediction: {data['accent']} with score {data['score']}")
            else:
                st.error(data.get("detail", "Something went wrong."))
                logging.error(f"API Error: {data}")

        except Exception as e:
            st.error(f"Request failed: {str(e)}")
            logging.exception("Exception occurred during API call.")
