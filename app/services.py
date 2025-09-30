import os
import requests
from dotenv import load_dotenv

# cargo variables desde el archivo .env
load_dotenv()

# defino url del modelo en hf
API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

# leo el token de hf de las variables de entorno
HF_API_KEY = os.getenv("HF_API_KEY")
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def analyze_sentiment(text: str):
    """
    Llama al endpoint de Hugging Face y devuelve el sentimiento más probable.
    """
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        data = response.json()
    except Exception:
        return {"label": "ERROR", "score": 0.0, "explanation": "Respuesta inválida del servidor"}

    # caso tipico, lista dentro de lista con varios labels
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
        results = data[0]
        best = max(results, key=lambda r: r["score"])
        explanation = f"El sentimiento detectado es {best['label'].lower()} con una confianza del {best['score']*100:.2f}%."
        return {"label": best["label"], "score": best["score"], "explanation": explanation}

    # hf devuelve error
    if isinstance(data, dict) and "error" in data:
        return {"label": "ERROR", "score": 0.0, "explanation": data["error"]}

    return {"label": "UNKNOWN", "score": 0.0, "explanation": "No se pudo determinar el sentimiento."}
