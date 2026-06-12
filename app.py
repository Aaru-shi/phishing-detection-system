import os
from flask import Flask, render_template, request
import pickle
import cv2
import numpy as np

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(
    open(os.path.join(BASE_DIR, "phishing.pkl"), "rb")
)

vectorizer = pickle.load(
    open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb")
)



def analyze_url(url):

    reasons = []

    if len(url) > 50:
        reasons.append("Long URL detected")

    if url.count('.') > 3:
        reasons.append("Too many dots in URL")

    if "@" in url:
        reasons.append("Contains @ symbol")

    if "-" in url:
        reasons.append("Contains hyphen (-)")

    if not url.startswith("https"):
        reasons.append("Website is not using HTTPS")

    suspicious_words = [
        "login",
        "verify",
        "bank",
        "secure",
        "account",
        "update",
        "paypal"
    ]

    for word in suspicious_words:
        if word in url.lower():
            reasons.append(f"Suspicious keyword found: {word}")

    if len(reasons) == 0:
        reasons.append("No suspicious patterns detected")

    return reasons



def detect_url(url):

    url_vector = vectorizer.transform([url])

    prediction = model.predict(url_vector)

    try:
        probability = model.predict_proba(url_vector)
        confidence = round(max(probability[0]) * 100, 2)
    except:
        confidence = "N/A"

    if prediction[0] == 1:
        result = "🚨 Phishing Website Detected"
    else:
        result = "✅ Safe Website"

    reasons = analyze_url(url)

    return result, confidence, reasons



@app.route('/')
def home():
    return render_template("index.html")



@app.route('/predict', methods=['POST'])
def predict():

    url = request.form['url']

    result, confidence, reasons = detect_url(url)

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence,
        reasons=reasons,
        checked_url=url
    )



@app.route('/scan_qr', methods=['POST'])
def scan_qr():

    try:

        image = request.files['qr_image']

        file_bytes = np.frombuffer(
            image.read(),
            np.uint8
        )

        img = cv2.imdecode(
            file_bytes,
            cv2.IMREAD_COLOR
        )

        detector = cv2.QRCodeDetector()

        qr_data, bbox, _ = detector.detectAndDecode(img)

        if not qr_data:

            return render_template(
                "index.html",
                prediction="❌ No QR Code Found",
                confidence="N/A",
                checked_url=""
            )

        url = qr_data

        result, confidence, reasons = detect_url(url)

        return render_template(
            "index.html",
            prediction=result,
            confidence=confidence,
            reasons=reasons,
            checked_url=url
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}"
        )



if __name__ == '__main__':
    app.run(debug=True)