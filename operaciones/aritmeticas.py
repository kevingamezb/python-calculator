# Operaciones Aritméticas (Suma, Resta, Multiplicación, División) - Shalon León
"""
Las cuatro reciben DOS números y hacen una operación con ellos.

Fíjate en el atributo `etiqueta`: es el texto que se muestra en el menú.
Fíjate en `entradas`: es una lista de (etiqueta, tipo) que le dice a la
consola qué pedir y en qué orden. Las cuatro aritméticas piden lo mismo:
dos números (por eso repiten la misma línea). Ver nucleo/operacion.py
para la explicación de estos atributos.

Importamos la clase base `Operacion` desde el paquete nucleo (la lógica
central). El prefijo nucleo. indica que el archivo está en la carpeta
nucleo/, así Python sabe dónde buscarla.
"""

from nucleo.operacion import Operacion
from excepciones.error_calculadora import ErrorDivisionPorCero

class Division(Operacion):
    etiqueta = 'División'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        # Guardamos los dos números como atributos de la instancia
        # (con guion bajo al inicio) para usarlos después en ejecutar().
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        # La división entre 0 no existe en matemáticas. En vez de dejar
        # que Python lance ZeroDivisionError, lanzamos nuestro propio
        # error para que la consola lo muestre bonito (ver
        # excepciones/error_calculadora.py).
        if self._numero_b == 0:
            raise ErrorDivisionPorCero()
        return self._numero_a / self._numero_b

class Suma(Operacion):
    etiqueta = 'Suma'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        return self._numero_a + self._numero_b

class Resta(Operacion):
    etiqueta = 'Resta'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        return self._numero_a - self._numero_b

class Multiplicacion(Operacion):
    etiqueta = 'Multiplicación'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        return self._numero_a * self._numero_b
