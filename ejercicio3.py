import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # Cargar variables de entorno
API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar cliente
client = genai.Client(api_key=API_KEY)

# Configuración del modelo (vendedor amable)
configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    system_instruction="""Eres un vendedor amable de una tienda de tecnología.
Respondes con claridad, especificaciones útiles y tono cordial.
Ayudas a los clientes a elegir productos tecnológicos según sus necesidades."""
)

# Historial few-shot (ejemplos precargados)
history = [
    {
        "role": "user",
        "parts": [{"text": "¿Qué características tiene el iPhone 14?"}]
    },
    {
        "role": "model",
        "parts": [{"text": "¡Con gusto! 😊 El iPhone 14 cuenta con pantalla Super Retina XDR de 6.1 pulgadas, chip A15 Bionic, cámara dual de 12 MP con modo noche y excelente rendimiento en batería. Es ideal si buscas potencia y fotografía de alta calidad."}]
    },
    {
        "role": "user",
        "parts": [{"text": "¿Tienen laptops para estudio?"}]
    },
    {
        "role": "model",
        "parts": [{"text": "¡Claro! 💻 Para estudio recomendamos laptops con procesador Intel i5 o Ryzen 5, 8-16 GB de RAM y SSD de 512 GB. Son rápidas, ligeras y perfectas para tareas académicas y videollamadas."}]
    }
]

# Inicialización del chat con historial
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=configuration,
    history=history
)

print("--- Chat de Soporte Tienda Tecnología ---")
print("(Escribe 'finalizar' para terminar)\n")

while True:
    user_input = input("Cliente: ")

    if user_input.lower() == "finalizar":
        print("Vendedor: ¡Gracias por visitar nuestra tienda! 😊 ¡Que tengas un excelente día!")
        break

    try:
        response = chat.send_message(user_input)
        print(f"\nVendedor: {response.text}\n")

    except Exception as e:
        print(f"Error al procesar la solicitud: {e}")
