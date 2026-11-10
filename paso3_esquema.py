"""Paso 3: obligar al modelo a seguir el esquema de Pydantic."""
from datetime import date

from llm import MODELO, cliente
from modelos import Pedido

mensaje = (
    """
Hola, Soy Andres de la empresa Datos Dinamicos. quiero un taller de capacitacion para 10 personas
no se si se puede a final del 2027. Quedo atento me confirmas
    """
)

respuesta = cliente.chat.completions.create(
    model=MODELO,
    temperature=0,
    messages=[
        {"role": "system", "content": f"Extrae el pedido del mensaje. Hoy es {date.today()}."},
        {"role": "user", "content": mensaje},
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {"name": "Pedido", "schema": Pedido.model_json_schema()},
    },
)

pedido = Pedido.model_validate_json(respuesta.choices[0].message.content)
print(pedido)
print(
    "Datos del pedido:\n"
    f"Cliente: {pedido.cliente}\n"
    f"Cantidad: {pedido.cantidad}\n"
    f"Fecha de entrega: {pedido.fecha_entrega}"
)
