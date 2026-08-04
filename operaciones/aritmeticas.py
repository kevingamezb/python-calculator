# Operaciones Aritméticas (Suma, Resta, Multiplicación, División) - Shalon León

from nucleo.operacion import Operacion
from excepciones.error_calculadora import ErrorDivisionPorCero

class Division(Operacion):
    etiqueta = 'División'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
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
