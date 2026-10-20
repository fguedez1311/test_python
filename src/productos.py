from dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    precio: float


if __name__ == "__main__":
    p1 = Producto("Lapiz", 1.5)
    p2 = Producto("Cuaderno", 2.5)
    print(p1)
    print(p2)
