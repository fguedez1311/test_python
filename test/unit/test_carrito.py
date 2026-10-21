# tests/unit/test_carrito.py
from tienda.carrito import Carrito
from tienda.productos import Producto


def test_carrito_vacio_tiene_total_cero():

    assert Carrito().total() == 0


def test_total_suma_precios():
    carrito = Carrito()
    carrito.agregar(Producto("Lápiz", 1.5))
    carrito.agregar(Producto("Cuaderno", 3.0))
    assert carrito.total() == 4.5
