# English Accent Classifier

A proof-of-concept web application that detects English accents from publicly shared video URLs using machine learning. The application combines a FastAPI backend with a Streamlit frontend to provide real-time accent classification with confidence scores.

## Features

- **Video URL Processing**: Input public video URLs (Loom, MP4 files, etc.)
- **Audio Extraction**: Automatic audio extraction and preprocessing
- **Accent Classification**: AI-powered accent detection using pretrained models
- **Confidence Scoring**: Returns prediction confidence alongside results
- **Modern Architecture**: FastAPI backend with Streamlit frontend
- **Real-time Analysis**: Fast processing and immediate results



## Project Structure

```
accent-detector/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── inference.py            # Accent classification logic
│   └── utils/
│       └── media_utils.py      # Audio processing utilities
├── frontend/
│   └── app.py                  # Streamlit interface
├── Pipfile                     # Dependencies
└── README.md
```

## Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/WaliBandawu/Accent-Detector.git
   cd Accent-Detector
   ```

2. **Install dependencies**
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```

## Usage

### Starting the Application

1. **Launch the backend server**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`

2. **Start the frontend interface**
   ```bash
   cd frontend
   streamlit run app.py
   ```
   Access the web interface at `http://localhost:8501`

### Using the Classifier

1. Navigate to the Streamlit interface
2. Enter a public video URL in the input field
3. Click the "Analyze" button
4. View the predicted accent and confidence score

### Testing the Application

You can test the application using these sample audio files:

**Sample 1 (American English):**
```
https://rr1---sn-cp1oxu-ngbl.googlevideo.com/videoplayback?expire=1748039214&ei=zqEwaOXZELqRssUPkfep4AE&ip=112.78.156.216&id=o-AI73axkEVocvsa_RsNk0Z6yWmZLNrz8Sjr9WqtdGKRQB&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1748017614%2C&mh=pn&mm=31%2C29&mn=sn-cp1oxu-ngbl%2Csn-npoeened&ms=au%2Crdu&mv=m&mvi=1&pl=24&rms=au%2Cau&initcwndbps=1046250&bui=AecWEAaeKC1d0Wsr-Vws-u4WQAXL8js5K6d7-OL3Fqmbbba-vW-f7NyDk6lwSK8oTdmbI4PcYJdFozKQ&vprv=1&svpuc=1&mime=video%2Fmp4&ns=dpWpfRDuntuRKPrISOZ2oMMQ&rqh=1&gir=yes&clen=1938314&ratebypass=yes&dur=45.139&lmt=1726511538918610&mt=1748017279&fvip=4&lmw=1&c=TVHTML5&sefc=1&txp=5538434&n=dpzKtVoJojJg7Q&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIhAOtV6yLvnFiNQzlls4lpbmcggPBBI9owgkXeVT2xCMjTAiA9Fdwsjlqwqad2qMqGr5TyFTTCdCDQ4D6RhraPdZSdPA%3D%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACuhMU0wRgIhAPxo3Fp6u9RBSzVHbQ1rnSTt3TiJVfmdF4OaNTzzqDZHAiEA-cWfkxfZ7FyzUfMsujQDX2MzaKrBjUvlezkEry8ZKnc%3D&title=Write%20Like%20A%20Winner%20%7C%20Write%20Your%20Best%20Work%20With%20Grammarly
```


> **Note:** This is a link that allows download.

## Requirements

```
streamlit
fastapi
uvicorn
requests
torchaudio
pydantic
```

## API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive API documentation.

## Limitations

- Supports only publicly accessible video URLs
- Requires downloadable media files
- Limited to English accent variants

## Roadmap

- [ ] File upload support for local media
- [ ] Enhanced error handling and validation
- [ ] Model fine-tuning capabilities
- [ ] Docker containerization
- [ ] Additional language support
- [ ] Batch processing functionality

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

Built by Waliyyullah Bandawu

---

*For questions or support, please open an issue on GitHub.*