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

<img width="1858" height="1004" alt="Captura de pantalla 2026-02-17 195821" src="https://github.com/user-attachments/assets/6263061d-2fd9-42b0-ba07-470715c5d160" />


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
texto = """El crecimiento acelerado de las ciudades en las últimas décadas ha generado importantes desafíos ambientales. 
Uno de los más relevantes es el aumento de la contaminación del aire..."""
resultado = procesar_articulo(texto, "resumir")
print(resultado)

<img width="1725" height="585" alt="Captura de pantalla 2026-02-17 202120" src="https://github.com/user-attachments/assets/c13ece31-48b6-4021-b84e-387b766a917b" />

<img width="1855" height="945" alt="Captura de pantalla 2026-02-17 202514" src="https://github.com/user-attachments/assets/fdd6a6cd-a397-4bdc-a384-160cf486347c" />

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

<img width="1786" height="501" alt="Captura de pantalla 2026-02-17 202226" src="https://github.com/user-attachments/assets/60d18cb5-d290-4682-8811-22fffff4908e" />
<img width="1863" height="1007" alt="Captura de pantalla 2026-02-17 202344" src="https://github.com/user-attachments/assets/9d07ba39-aaed-41ae-9532-6011f0d9d37f" />
<img width="1643" height="514" alt="Captura de pantalla 2026-02-17 202239" src="https://github.com/user-attachments/assets/fe098ef7-c02d-4a93-a37d-2bab2c489d5b" />


