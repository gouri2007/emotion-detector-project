import json
import requests

API_URL = "https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/XXXX"
API_KEY = "YOUR_API_KEY_HERE"

def emotion_detector(text_to_analyze: str) -> dict:
    """
    Calls Watson NLP emotion API and returns a dict with emotions and dominant emotion.
    """
    if not text_to_analyze:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    url = f"{API_URL}/v1/analyze?version=2021-08-01"
    headers = {"Content-Type": "application/json"}
    payload = {
        "text": text_to_analyze,
        "features": {
            "emotion": {}
        }
    }

    response = requests.post(url, headers=headers, auth=("apikey", API_KEY), json=payload)

    if response.status_code != 200:
        # You’ll refine this in Task 7
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    result = response.json()
    emotions = result["emotion"]["document"]["emotion"]

    dominant = max(emotions, key=emotions.get)

    return {
        "anger": emotions.get("anger"),
        "disgust": emotions.get("disgust"),
        "fear": emotions.get("fear"),
        "joy": emotions.get("joy"),
        "sadness": emotions.get("sadness"),
        "dominant_emotion": dominant,
    }
