# 🎹 English Accent Classifier

This is a proof-of-concept web application that detects **English accents** from publicly shared video URLs (e.g., Loom or MP4 files). It uses a combination of:

* `Streamlit` for the frontend
* `FastAPI` for backend inference
* `SpeechBrain` + `torchaudio` for audio processing and accent classification

---

## 📦 Features

* 🌐 Input a video URL (e.g., Loom, MP4 link)
* 🎿 Audio is extracted and processed
* 🧠 Accent is predicted using a pretrained speech classification model
* 📈 Confidence score returned alongside the result
* 🔀 FastAPI-powered backend
* 🖥️ Streamlit frontend interface

---

## 📁 Project Structure

```
accent-detector/
│
├── backend/
│   ├── main.py                 # FastAPI app
│   ├── inference.py            # Accent analysis logic
│   └── utils/
│       └── audio_utils.py      # Audio download & extraction
│
├── frontend/
│   └── app.py                  # Streamlit app
│
├── Pipfile                    # Project dependencies
└── README.md                  # You're reading it!
```

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/accent-detector.git
cd accent-detector
```

### 2. Install dependencies

Make sure you have Python 3.11 installed.

```bash
pip install pipenv
pipenv install
pipenv shell
```

---

## 🚀 Running the App

### 1. Start the backend server

```bash
cd backend
uvicorn main:app --reload
```

This starts the FastAPI server at `http://localhost:8000`.

### 2. Run the frontend

In a new terminal:

```bash
cd frontend
streamlit run app.py
```

Visit `http://localhost:8501` to interact with the app.

---

## 🧪 Example Usage

1. Paste a public Loom or MP4 video URL in the Streamlit UI.
2. Click **"Analyze"**.
3. Wait for analysis.
4. Get the **predicted accent** and **confidence score**.

---

## 🛡️ Requirements

* Python 3.11+
* streamlit
* fastapi
* uvicorn
* requests
* torchaudio
* pydantic

---

## 📝 Notes

* The model is a pretrained `SpeechBrain` classifier.
* Only public video URLs are supported (must be downloadable).

---

## 📌 To-Do

* [ ] Add support for uploading video/audio files
* [ ] Improve error handling
* [ ] Add model fine-tuning options
* [ ] Dockerize app for deployment

---

## 📄 License

MIT License. Built with ❤️ by Waliyyullah Bandawu.

