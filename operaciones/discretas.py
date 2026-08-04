# Operaciones Discretas (Factorial, Fibonacci, Mínimo Común Múltiplo, Máximo Común Divisor) - Andrés León [Alvaro Orjuela (Factorial)]

from nucleo.operacion import Operacion
from excepciones.error_calculadora import ErrorFactorialNegativo

class Factorial(Operacion):
    etiqueta = 'Factorial'

    def __init__(self, numero_a):
        self._numero_a = numero_a

    def ejecutar(self):
        if self._numero_a < 0:
            raise ErrorFactorialNegativo
        if self._numero_a == 0 or self._numero_a == 1:
            return 1
        return self._numero_a * Factorial(self._numero_a-1)
