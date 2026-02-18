PARTICIPANTES:
Lina Sofia Cortes Hernandez
Laura Daniela Galindo Casallas

📘 Ejercicio 1 – Consulta simple a Gemini

Script que inicializa el cliente de Gemini y realiza una consulta básica para explicar el concepto de Inferencia en IA en menos de 50 palabras.

Objetivo

Aprender a:

Inicializar el cliente

Enviar un prompt

Recibir la respuesta del modelo

<img width="1561" height="771" alt="image" src="https://github.com/user-attachments/assets/d56fd3e4-22f8-40bb-ba64-0489da95430c" />


Ejecución
python ejercicio1.py
📄 Ejercicio 2 – Procesador de Textos Inteligente

Función procesar_articulo(texto, tarea) que permite:

resumir → genera resumen ejecutivo

profesionalizar → convierte el texto en tono formal y técnico

Usa system_instruction para definir a la IA como:

Editor Editorial de prestigio

Ejecución
python ejercicio2.py
Ejemplo de uso
texto = """La inteligencia artificial está transformando múltiples industrias..."""
resultado = procesar_articulo(texto, "resumir")
print(resultado)
💬 Ejercicio 3 – Chat de Soporte con Historial (Few‑Shot)

Sistema de chat para una tienda de tecnología con:

Rol: vendedor amable

Historial precargado (few‑shot)

Conversación continua hasta escribir finalizar

Características

Recomienda productos tecnológicos

Responde con especificaciones

Mantiene contexto conversacional

Ejecución
