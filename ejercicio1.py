# Script: Consulta simple a Gemini sobre Inferencia en IA
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Cargar la API Key desde .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Inicializar cliente Gemini
client = genai.Client(api_key=api_key)

# 3. Configuración de generación (máx 50 palabras)
config = types.GenerateContentConfig(
    temperature=0.3,
    max_output_tokens=1000
)

# 4. Consulta simple
prompt = "Explica qué es la inferencia en IA en menos de 50 palabras."

# 5. Llamada al modelo
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt,
    config=config
)

# 6. Mostrar respuesta
print("Respuesta del modelo:")
for part in response.candidates[0].content.parts:
    if hasattr(part, "text") and part.text:
        print(part.text, end="")
