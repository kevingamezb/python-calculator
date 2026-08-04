# Operaciones Discretas (Factorial, Fibonacci, Mínimo Común Múltiplo, Máximo Común Divisor) - Andrés León [Alvaro Orjuela (Factorial)]

from nucleo.operacion import Operacion
from excepciones.error_calculadora import (
    ErrorEntradaNoValida,
    ErrorFactorialNegativo,
    ErrorFactorialNoEntero,
    ErrorFibonacciNegativo,
)


def _es_entero_positivo(numero):
    """True si el número es un entero mayor que cero (12 y 12.0 valen)."""
    return float(numero).is_integer() and numero > 0


class Factorial(Operacion):
    etiqueta = 'Factorial'

    def __init__(self, numero_a):
        self._numero_a = numero_a

    def ejecutar(self):
        if self._numero_a < 0:
            raise ErrorFactorialNegativo()

        if not float(self._numero_a).is_integer():
            raise ErrorFactorialNoEntero()

        if self._numero_a == 0 or self._numero_a == 1:
            return 1

        # Falta el () al final: sin él, multiplicábamos por el OBJETO
        # Factorial (TypeError) en vez de por su resultado.
        return self._numero_a * Factorial(self._numero_a - 1)()


class MCM(Operacion):
    etiqueta = 'Mínimo Común Múltiplo'

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        for numero in (self._numero_a, self._numero_b):
            if not _es_entero_positivo(numero):
                raise ErrorEntradaNoValida("El MCM solo está definido para enteros positivos.")

        # MCM(a, b) = a * b // MCD(a, b). Nota: antes había un __int__
        # (no __init__) y el cuerpo era el algoritmo de Euclides (eso es
        # MCD), así que nunca se llegaba al resultado correcto.
        mcd = MCD(self._numero_a, self._numero_b).ejecutar()
        return self._numero_a * self._numero_b // mcd


class MCD(Operacion):
    etiqueta = 'Máximo Común Divisor'

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        for numero in (self._numero_a, self._numero_b):
            if not _es_entero_positivo(numero):
                raise ErrorEntradaNoValida("El MCD solo está definido para enteros positivos.")

        a, b = self._numero_a, self._numero_b
        while b != 0:
            a, b = b, a % b
        return a


class Fibonacci(Operacion):
    etiqueta = 'Fibonacci'

    def __init__(self, numero):
        self._numero = numero

    def ejecutar(self):
        n = self._numero

        if n < 0:
            raise ErrorFibonacciNegativo()

        if not float(n).is_integer():
            raise ErrorEntradaNoValida("El fibonacci solo está definido para enteros.")

        if n == 0:
            return 0

        if n == 1:
            return 1

        a, b = 0, 1

        for _ in range(1, n):
            a, b = b, a + b

        # El return va FUERA del for: dentro, devolvía el primer paso (1)
        # sin importar cuántos términos se pidieran.
        return b
