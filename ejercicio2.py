import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Inicializar el cliente de Gemini
client = genai.Client(api_key=API_KEY)

def procesar_articulo(texto, tarea):
    """
    Procesa un artículo según la tarea especificada.

    Args:
        texto (str): El texto largo que se desea procesar.
        tarea (str): La tarea a realizar, puede ser "resumir" o "profesionalizar".

    Returns:
        str: El texto procesado según la tarea.
    """
    # Validar entrada
    if not texto.strip():
        return "El texto no puede estar vacío."

    # Definir la system_instruction
    system_instruction = "Eres un Editor Editorial de prestigio."

    # Crear el prompt según la tarea
    if tarea == "resumir":
        prompt = f"Por favor, resume el siguiente texto:\n{texto}"
    elif tarea == "profesionalizar":
        prompt = f"Por favor, edita el siguiente texto para que suene formal y técnico:\n{texto}"
    else:
        return "Tarea no válida. Debe ser 'resumir' o 'profesionalizar'."

    # Configuración del modelo
    configuration = types.GenerateContentConfig(
        max_output_tokens=1000,  # Aumenta el límite de tokens
        system_instruction=system_instruction
    )

    try:
        # Realizar la petición a la API
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=configuration,
            contents=prompt
        )
        return response.text.strip()  # Devolver el texto procesado
    except Exception as e:
        return f"❌ Error al procesar el artículo: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    texto = """
El crecimiento acelerado de las ciudades en las últimas décadas ha generado importantes desafíos ambientales. 
Uno de los más relevantes es el aumento de la contaminación del aire, provocado principalmente por el transporte 
vehicular y las actividades industriales. Esta situación afecta directamente la salud de los habitantes urbanos, 
incrementando enfermedades respiratorias y cardiovasculares. Además, la expansión urbana desordenada ha reducido 
las áreas verdes, lo que disminuye la capacidad natural de las ciudades para absorber dióxido de carbono y regular 
la temperatura. Como consecuencia, se intensifica el fenómeno de las islas de calor urbanas, donde las temperaturas 
son significativamente más altas que en zonas rurales cercanas. Frente a este panorama, muchas ciudades están 
implementando estrategias de sostenibilidad, como la promoción del transporte público eléctrico, la creación de 
corredores verdes y el uso de energías renovables en la infraestructura urbana. Estas medidas buscan mejorar la 
calidad de vida de los ciudadanos y reducir el impacto ambiental de las actividades humanas en entornos urbanos.
"""

    tarea = "resumir"  # Cambiar a "profesionalizar" para probar
    print(f"Tarea seleccionada: {tarea}")
    resultado = procesar_articulo(texto, tarea)
    print("\nResultado:")
    print(resultado)