# imagen base de Python
FROM python:3.11-slim

# directorio de trabajo
WORKDIR /code

# copiar requirements
COPY requirements.txt .

# instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# copiar el resto del proyecto
COPY . .

# exponer puerto 
EXPOSE 7860

# comando para iniciar FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
