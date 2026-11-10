"""Versión final: esquema + validación + reintento con el error como pista."""
from datetime import date

from pydantic import ValidationError

from llm import MODELO, cliente
from modelos import Pedido


def extraer_pedido(mensaje: str, intentos: int = 3) -> Pedido:
    mensajes = [
        {"role": "system", "content": f"Extrae el pedido del mensaje. Hoy es {date.today()}."},
        {"role": "user", "content": mensaje},
    ]
    for intento in range(1, intentos + 1):
        respuesta = cliente.chat.completions.create(
            model=MODELO,
            temperature=0,
            messages=mensajes,
            response_format={
                "type": "json_schema",
                "json_schema": {"name": "Pedido", "schema": Pedido.model_json_schema()},
            },
        )
        texto = respuesta.choices[0].message.content
        try:
            return Pedido.model_validate_json(texto)
        except ValidationError as e:
            print(f"Intento {intento} falló, reintentando con el error...")
            # Le mostramos al modelo su respuesta y el error para que la corrija
            mensajes.append({"role": "assistant", "content": texto})
            mensajes.append({"role": "user", "content": f"Tu JSON no es válido:\n{e}\nCorrígelo."})
    raise ValueError(f"No se pudo extraer un pedido válido en {intentos} intentos")


if __name__ == "__main__":
    print(extraer_pedido("Buenas, soy Carlos de Pasto, mándame 2 bultos de papa pastusa cuando puedas"))
