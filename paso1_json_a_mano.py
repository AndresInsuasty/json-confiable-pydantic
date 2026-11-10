"""Paso 1: pedir JSON "por favor" y ver por qué no es confiable."""
import json

from llm import MODELO, cliente

mensaje = (
    "Hola! soy Laura Gómez, necesito 3 cajas de café de Nariño "
    "para el viernes en Medellín, es urgente porfa"
)

respuesta = cliente.chat.completions.create(
    model=MODELO,
    messages=[
        {"role": "system", "content": "Extrae el pedido del mensaje y responde en JSON."},
        {"role": "user", "content": mensaje},
    ],
)
texto = respuesta.choices[0].message.content
print(texto)

try:
    datos = json.loads(texto)
    print("\nJSON válido:", datos)
    # Aunque sea JSON válido: ¿las claves se llaman igual siempre? ¿cantidad es 3 o "tres"?
except json.JSONDecodeError as e:
    print("\nNo es JSON válido:", e)
