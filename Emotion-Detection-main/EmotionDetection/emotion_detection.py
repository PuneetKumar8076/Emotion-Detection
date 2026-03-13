def emotion_detector(text_to_analyse):

    emotions = {
        "anger": 0.02,
        "disgust": 0.01,
        "fear": 0.01,
        "joy": 0.94,
        "sadness": 0.02
    }

    dominant_emotion = max(emotions, key=emotions.get)

    emotions["dominant_emotion"] = dominant_emotion

    return emotions