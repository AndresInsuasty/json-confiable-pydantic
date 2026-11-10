"""Demo del video: varios mensajes desordenados -> tabla de pedidos + pedidos.json."""
import json
from pathlib import Path

from extractor import extraer_pedido

mensajes = Path("data/mensajes.txt").read_text(encoding="utf-8").strip().split("\n\n")

pedidos = []
for m in mensajes:
    try:
        pedidos.append(extraer_pedido(m))
    except ValueError as e:
        print(f"Saltado: {m[:40]}... ({e})")

print(f"\n{'Cliente':<18}{'Producto':<26}{'Cant':>5}  {'Ciudad':<12}{'Entrega':<12}Urgente")
for p in pedidos:
    print(
        f"{p.cliente:<18}{p.producto[:25]:<26}{p.cantidad:>5}  "
        f"{(p.ciudad or '-'):<12}{str(p.fecha_entrega or '-'):<12}{'sí' if p.urgente else 'no'}"
    )

Path("pedidos.json").write_text(
    json.dumps([p.model_dump(mode="json") for p in pedidos], ensure_ascii=False, indent=2),
    encoding="utf-8",
)
print(f"\n{len(pedidos)} pedidos guardados en pedidos.json")
