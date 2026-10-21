from .productos import Producto


class Carrito:
    def __init__(self):
        self._items: list[Producto] = []

    def agregar(self, producto: Producto) -> None:
        self._items.append(producto)

    def total(self) -> float:
        return sum(p.precio for p in self._items)
