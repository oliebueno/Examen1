# Importar la librería pytest
import pytest
# Importar la clase BuddySystem desde el archivo ejer3.py
from ejer3 import BuddySystem

# Definir una función auxiliar para crear una instancia de la clase BuddySystem con 16 bloques de memoria


def crear_buddy_system():
    return BuddySystem(16)

# Definir una función de prueba para el método reservar


def test_reservar():
    # Crear una instancia de la clase BuddySystem
    bs = crear_buddy_system()
    # Reservar 3 bloques para el identificador A y verificar que se actualicen las listas libres y el diccionario de nombres
    bs.reservar(3, "A")
    assert bs.listas_libres == [[], [], [(4, 7)], [(8, 15)], []]
    assert bs.nombres_re == {"A": (0, 3)}
    # Reservar 4 bloques para el identificador B y verificar que se actualicen las listas libres y el diccionario de nombres
    bs.reservar(4, "B")
    assert bs.listas_libres == [[], [], [], [(8, 15)], []]
    assert bs.nombres_re == {"A": (0, 3), "B": (4, 7)}
    # Intentar reservar 9 bloques para el identificador C y verificar que se muestre un mensaje de error y no se modifiquen las listas libres ni el diccionario de nombres
    # Try to reserve 4 blocks for "B" (should fail)
    try:
        bs.reservar(9, "C")
    except Exception as e:
        assert str(
            e) == "Error: No hay espacio suficiente para reservar 4 bloques para B."

    assert bs.listas_libres == [[], [], [], [(8, 15)], []]
    assert bs.nombres_re == {"A": (0, 3), "B": (4, 7)}

    try:
        bs.reservar(2, "B")
    except Exception as e:
        assert str(
            e) == "Error: B ya tiene espacio reservado"

    assert bs.listas_libres == [[], [], [], [(8, 15)], []]
    assert bs.nombres_re == {"A": (0, 3), "B": (4, 7)}


def test_liberar():
    # Crear una instancia de la clase BuddySystem
    bs = crear_buddy_system()
    # Reservar algunos bloques para los identificadores A, B y C
    bs.reservar(3, "A")
    bs.reservar(4, "B")
    bs.reservar(2, "C")
    # Liberar el espacio reservado por el identificador A y verificar que se actualicen las listas libres y el diccionario de nombres
    bs.liberar("A")
    assert bs.listas_libres == [[], [(10, 11)], [(12, 15), (0, 3)], [], []]
    assert bs.nombres_re == {"B": (4, 7), "C": (8, 9)}
    # Liberar el espacio reservado por el identificador B y verificar que se actualicen las listas libres y el diccionario de nombres
    bs.liberar("B")
    assert bs.listas_libres == [[], [(10, 11)], [(12, 15)], [(0, 7)], []]
    assert bs.nombres_re == {"C": (8, 9)}
    # Liberar el espacio reservado por el identificador C y verificar que se actualicen las listas libres y el diccionario de nombres
    bs.liberar("C")
    assert bs.listas_libres == [[], [], [], [], [(0, 15)]]
    assert bs.nombres_re == {}
    # Intentar liberar el espacio reservado por el identificador D y verificar que se muestre un mensaje de error y no se modifiquen las listas libres ni el diccionario de nombres
    try:
        bs.liberar("D")
    except Exception as e:
        assert str(
            e) == "Error: No hay memoria reservada para el identificador D"
    assert bs.listas_libres == [[], [], [], [], [(0, 15)]]
    assert bs.nombres_re == {}


def test_mostrar():
    bs = crear_buddy_system()

    bs.mostrar()
    assert bs.linea == "Memoria: |________________|"
    bs.reservar(3, "A")
    bs.mostrar()
    assert bs.linea == "Memoria: |[][][][]____________|"
    bs.reservar(4, "B")
    bs.mostrar()
    assert bs.linea == "Memoria: |[][][][][][][][]________|"
    bs.reservar(2, "C")
    bs.mostrar()
    assert bs.linea == "Memoria: |[][][][][][][][][][]______|"
    bs.liberar("A")
    bs.mostrar()
    assert bs.linea == "Memoria: |____[][][][][][]______|"
    bs.liberar("B")
    bs.mostrar()
    assert bs.linea == "Memoria: |________[][]______|"
    bs.liberar("C")
    bs.mostrar()
    assert bs.linea == "Memoria: |________________|"


def test_ejecutar(monkeypatch):
    bs = crear_buddy_system()
    entradas = (x for x in ["reservar 3 A", "reservar 4 B", "reservar 2 C",
                "liberar A", "liberar B", "liberar C", "mostrar", "salir"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    bs.ejecutar()
