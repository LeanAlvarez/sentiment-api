# 📊 Sentiment Analyzer API

API REST en **FastAPI** que analiza el sentimiento de un texto usando el modelo `distilbert-base-uncased-finetuned-sst-2-english` de Hugging Face, consumido a través del **Inference API**.  

---

## 🚀 Características
- Analiza texto en inglés y devuelve el sentimiento (`POSITIVE` o `NEGATIVE`).  
- Devuelve también el **score de confianza** y una **explicación en lenguaje natural**.  
- Arquitectura modular: `main.py`, `routes.py`, `services.py`, `models.py`.  
- Uso de **Pydantic** para validar requests/responses.  
- Variables de entorno con `.env` (para la API key de Hugging Face).  

---

## 📂 Estructura del proyecto
sentiment-api/
│── app/
│ │── main.py # Punto de entrada FastAPI
│ │── routes.py # Rutas de la API
│ │── services.py # Lógica con Hugging Face
│ │── models.py # Schemas Pydantic
│── .env # Variables de entorno (HF_API_KEY)
│── requirements.txt # Dependencias


## ⚙️ Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/sentiment-api.git
cd sentiment-api
2. Crear un entorno virtual

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Instalar dependencias

pip install -r requirements.txt
4. Configurar Hugging Face API Key
Crear un archivo .env en la raíz:


HF_API_KEY=tu_token_de_huggingface
Conseguí el token en Hugging Face Settings → Access Tokens.

Asegurase que sea de tipo Read.

▶️ Ejecución
Levantar el servidor local:

uvicorn app.main:app --reload
El servidor corre en:
http://127.0.0.1:8000

Documentación interactiva:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🧪 Ejemplo de uso

Request
curl -X 'POST' \
  'http://127.0.0.1:8000/api/sentiment' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "I love this product"
}'

Response

{
  "label": "POSITIVE",
  "score": 0.9998788833618164,
  "explanation": "El sentimiento detectado es positive con una confianza del 99.99%."
}
🛠️ Tecnologías
FastAPI

Pydantic

Requests

Hugging Face Inference API

📌 Próximos pasos
Agregar soporte multi-idioma (ej: modelo multilingüe).

Permitir batch de frases (procesar varias de una vez).

Deploy en Hugging Face Spaces / Render.

✍️ Desarrollado por Leandro Alvarez

