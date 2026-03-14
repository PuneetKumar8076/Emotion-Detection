"""Emotion Detection Flask Server"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def detect_emotion():
    """Analyze text emotion using Watson NLP"""

    text = request.args.get('textToAnalyze')

    if text is None or text.strip() == "":
        return "Invalid text! Please try again."

    response = emotion_detector(text)

    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
