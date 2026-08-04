# Operaciones Discretas (Factorial, Fibonacci, Mínimo Común Múltiplo, Máximo Común Divisor) - Andrés León [Alvaro Orjuela (Factorial)]
"""
Operaciones con números enteros.

Nota sobre los números que llegan de la consola: la consola convierte
lo que escribe el usuario a float (ej. "5" se vuelve 5.0). Estas
operaciones exigen enteros, así que validamos con
`float(numero).is_integer()`: devuelve True si el número es entero,
tanto para 5 (tipo int) como para 5.0 (tipo float).
"""

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
    entradas = [('Número', 'numero')]

    def __init__(self, numero_a):
        self._numero_a = numero_a

    def ejecutar(self):
        # El factorial de un número negativo no existe.
        if self._numero_a < 0:
            raise ErrorFactorialNegativo()

        # El factorial solo está definido para enteros: 2.5! no existe.
        if not float(self._numero_a).is_integer():
            raise ErrorFactorialNoEntero()

        # Casos base de la recursión: 0! = 1 y 1! = 1.
        if self._numero_a == 0 or self._numero_a == 1:
            return 1

        # RECURSIÓN: un método que se llama a sí mismo. El factorial
        # cumple la propiedad: n! = n * (n-1)!
        #   Ejemplo: 5! = 5 * 4! = 5 * 4 * 3! = ... = 5 * 4 * 3 * 2 * 1
        # El () al final llama a __call__ de Operacion (que llama a
        # ejecutar): sin él, multiplicaríamos por el OBJETO Factorial
        # (TypeError) en vez de por su resultado.
        return self._numero_a * Factorial(self._numero_a - 1)()


class MCM(Operacion):
    etiqueta = 'Mínimo Común Múltiplo'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        for numero in (self._numero_a, self._numero_b):
            if not _es_entero_positivo(numero):
                raise ErrorEntradaNoValida("El MCM solo está definido para enteros positivos.")

        # Fórmula: MCM(a, b) = a * b / MCD(a, b)
        #   Ejemplo: MCM(12, 18) = 12 * 18 / MCD(12, 18) = 216 / 6 = 36
        # Reutilizamos la clase MCD (definida más abajo), que ya sabe
        # cómo calcular el máximo común divisor.
        mcd = MCD(self._numero_a, self._numero_b).ejecutar()
        return self._numero_a * self._numero_b // mcd


class MCD(Operacion):
    etiqueta = 'Máximo Común Divisor'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        for numero in (self._numero_a, self._numero_b):
            if not _es_entero_positivo(numero):
                raise ErrorEntradaNoValida("El MCD solo está definido para enteros positivos.")

        # ALGORITMO DE EUCLIDES: para encontrar el MCD de a y b, se repite
        # "a, b = b, a % b" hasta que b sea 0. El a que queda es el MCD.
        #
        # Ejemplo con (12, 18):
        #   1ª vuelta: a = 18, b = 12 % 18 = 12   -> b = 12
        #   2ª vuelta: a = 12, b = 18 % 12 = 6    -> b = 6
        #   3ª vuelta: a = 6,  b = 12 % 6 = 0     -> b = 0, termina
        #   Resultado: a = 6  =  MCD(12, 18)
        #
        # % es el módulo: el residuo de la división entera.
        # La línea "a, b = b, a % b" hace los DOS cambios a la vez, usando
        # los valores VIEJOS de a y b para calcular el par nuevo.
        a, b = self._numero_a, self._numero_b
        while b != 0:
            a, b = b, a % b
        return a


class Fibonacci(Operacion):
    etiqueta = 'Fibonacci'
    entradas = [('Término', 'numero')]

    def __init__(self, numero):
        self._numero = numero

    def ejecutar(self):
        n = self._numero

        # La sucesión empieza en 0; no hay términos negativos.
        if n < 0:
            raise ErrorFibonacciNegativo()

        # Los términos son enteros; n = 4.5 no tiene sentido.
        if not float(n).is_integer():
            raise ErrorEntradaNoValida("El fibonacci solo está definido para enteros.")

        # La consola manda floats (10.0); range() exige int, así que
        # convertimos DESPUÉS de validar que es un entero.
        n = int(n)

        # La sucesión de Fibonacci empieza así: 0, 1, 1, 2, 3, 5, 8...
        # F(0) = 0 y F(1) = 1; los siguientes son la suma de los dos
        # anteriores. Estos dos `if` son los casos base.
        if n == 0:
            return 0

        if n == 1:
            return 1

        # A partir de F(2), vamos calculando término por término.
        # Empezamos guardando los dos primeros (0 y 1) en a y b.
        a, b = 0, 1

        # El for da n-1 vueltas. En cada vuelta, el término siguiente es
        # la suma de los dos anteriores: (a, b) pasa a ser (b, a + b).
        for _ in range(1, n):
            a, b = b, a + b

        # Cuando termina el for, b guarda el término n. Ejemplo con n = 5:
        #   1ª vuelta: a=1, b=1 | 2ª: a=1, b=2 | 3ª: a=2, b=3 | 4ª: a=3, b=5
        #   F(5) = 5
        return b
