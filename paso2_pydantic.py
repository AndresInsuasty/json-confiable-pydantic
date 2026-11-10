"""Paso 2: Pydantic sin LLM. Valida y convierte tipos, o falla con un error claro."""
from pydantic import ValidationError

from modelos import Pedido

# Llega texto, Pydantic convierte: "3" -> 3, "2026-11-13" -> date
bueno = '{"cliente": "Laura Gómez", "producto": "café", "cantidad": "3", "fecha_entrega": "2026-11-13", "urgente": true}'
pedido = Pedido.model_validate_json(bueno)
print(pedido)
print(type(pedido.cantidad), type(pedido.fecha_entrega))

# Datos que no cumplen el contrato
malo = '{"cliente": "Laura", "producto": "café", "cantidad": "tres", "urgente": "quizás"}'
try:
    Pedido.model_validate_json(malo)
except ValidationError as e:
    print("\n", e)

# El esquema que le vamos a pasar al modelo
print("\n", Pedido.model_json_schema())
