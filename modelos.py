"""El contrato: qué forma deben tener los datos que devuelve el modelo."""
from datetime import date

from pydantic import BaseModel, Field


class Pedido(BaseModel):
    cliente: str = Field(description="Nombre de quien hace el pedido")
    producto: str = Field(description="Qué quiere comprar")
    cantidad: int = Field(gt=0, description="Unidades pedidas, número entero mayor que 0")
    ciudad: str | None = Field(default=None, description="Ciudad de entrega, si la menciona")
    fecha_entrega: date | None = Field(
        default=None, description="Fecha de entrega en formato AAAA-MM-DD, si la menciona"
    )
    urgente: bool = Field(description="true si el cliente pide rapidez")
