# Operaciones Aritméticas (Suma, Resta, Multiplicación, División) - Shalon León
"""
Las cuatro operaciones aritméticas básicas, ahora como métodos de una
sola clase `Aritmetica` en vez de una clase por operación.

`OPERACIONES` es el registro que le dice a `nucleo/calculadora.py` qué
método llamar, cómo se etiqueta en el menú, y qué entradas pedir por
consola (mismo formato de tuplas (etiqueta, tipo) que antes vivía como
atributo `entradas` de cada clase-operación; ver nucleo/operacion.py).
"""

from excepciones.error_calculadora import ErrorDivisionPorCero

_ENTRADAS_DOS_NUMEROS = [('Primer número', 'numero'), ('Segundo número', 'numero')]


class Aritmetica:

    # clave del registro -> (nombre del método, etiqueta del menú, entradas)
    OPERACIONES = {
        'Suma':           ('sumar',       'Suma',           _ENTRADAS_DOS_NUMEROS),
        'Resta':          ('restar',      'Resta',          _ENTRADAS_DOS_NUMEROS),
        'Multiplicacion': ('multiplicar', 'Multiplicación', _ENTRADAS_DOS_NUMEROS),
        'Division':       ('dividir',     'División',       _ENTRADAS_DOS_NUMEROS),
    }

    def sumar(self, numero_a, numero_b):
        return numero_a + numero_b

    def restar(self, numero_a, numero_b):
        return numero_a - numero_b

    def multiplicar(self, numero_a, numero_b):
        return numero_a * numero_b

    def dividir(self, numero_a, numero_b):
        # La división entre 0 no existe en matemáticas. En vez de dejar
        # que Python lance ZeroDivisionError, lanzamos nuestro propio
        # error para que la consola lo muestre bonito.
        if numero_b == 0:
            raise ErrorDivisionPorCero()
        return numero_a / numero_b