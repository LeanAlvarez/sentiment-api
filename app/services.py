import os
import requests
from dotenv import load_dotenv

# Carga variables del .env
load_dotenv()
API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
HF_API_KEY = os.getenv("HF_API_KEY")
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def analyze_sentiment(text: str):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        data = response.json()
    except Exception:
        return {"label": "ERROR", "score": 0.0}

    # ✅ Caso típico: doble lista -> nos quedamos con el mejor resultado
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
        results = data[0]  # ahora es una lista de dicts con label y score
        best = max(results, key=lambda r: r["score"])
        return {"label": best["label"], "score": best["score"]}

    # 🚨 Si Hugging Face devuelve error
    if isinstance(data, dict) and "error" in data:
        return {"label": "ERROR", "score": 0.0}

    return {"label": "UNKNOWN", "score": 0.0}
