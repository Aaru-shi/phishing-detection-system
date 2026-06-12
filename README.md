# AI-Powered Phishing Website Detector

## Overview

An intelligent phishing detection system that identifies malicious websites using Machine Learning. Users can either enter a URL directly or upload a QR code image containing a URL for analysis.

The system provides:
- Phishing/Safe prediction
- Confidence score
- Explainable AI analysis
- QR code URL extraction

---

## Features

✅ URL Phishing Detection

✅ QR Code Phishing Detection

✅ Explainable AI Analysis

✅ Confidence Score

✅ User-Friendly Flask Web Interface

---

## Technologies Used

- Python
- Flask
- Scikit-Learn
- OpenCV
- NumPy
- HTML
- CSS

---

## Project Structure

```text
PHISHING DETECTION SYSTEM
│
├── templates
│   └── index.html
│
├── app.py
├── phishing.pkl
├── vectorizer.pkl
├── requirements.txt
├── Procfile
├── README.md
```

## How It Works

### URL Detection

1. User enters a URL.
2. URL is transformed using the saved vectorizer.
3. ML model predicts whether the URL is safe or phishing.
4. Confidence score and reasons are displayed.

### QR Code Detection

1. User uploads a QR code image.
2. OpenCV extracts the URL from the QR code.
3. Extracted URL is analyzed by the ML model.
4. Results are displayed to the user.

---

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Future Improvements

- Browser Extension
- Detection History Dashboard
- Risk Score Visualization
- Real-Time URL Monitoring
- Threat Intelligence Integration

---

## Author

Developed as a Machine Learning and Cybersecurity Project using Flask.