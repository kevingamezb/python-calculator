# Operaciones Discretas (Factorial, Fibonacci, MCM, MCD, IVA) - Andrés León [Alvaro Orjuela (Factorial)], IVA: Shalon León
"""
Operaciones con números enteros, más IVA (que antes vivía en su propio
archivo `impuestos.py`): se unen aquí porque, junto a Aritmética,
Exponencial y Trigonométrica, la calculadora ahora solo tiene 4
categorías de operación.

Nota sobre los números que llegan de la consola: la consola convierte
lo que escribe el usuario a float (ej. "5" se vuelve 5.0). Factorial,
Fibonacci, MCM y MCD exigen enteros, así que validamos con
`float(numero).is_integer()`: devuelve True si el número es entero,
tanto para 5 (tipo int) como para 5.0 (tipo float).
"""

from excepciones.error_calculadora import (
    ErrorEntradaNoValida,
    ErrorFactorialNegativo,
    ErrorFactorialNoEntero,
    ErrorFibonacciNegativo,
)

_ENTRADAS_UN_NUMERO = [('Número', 'numero')]
_ENTRADAS_DOS_NUMEROS = [('Primer número', 'numero'), ('Segundo número', 'numero')]


def _es_entero_positivo(numero):
    """True si el número es un entero mayor que cero (12 y 12.0 valen)."""
    return float(numero).is_integer() and numero > 0


class Discreta:

    OPERACIONES = {
        'Factorial': ('factorial', 'Factorial',                _ENTRADAS_UN_NUMERO),
        'Fibonacci': ('fibonacci', 'Fibonacci',                 _ENTRADAS_UN_NUMERO),
        'MCM':       ('mcm',       'Mínimo Común Múltiplo',     _ENTRADAS_DOS_NUMEROS),
        'MCD':       ('mcd',       'Máximo Común Divisor',      _ENTRADAS_DOS_NUMEROS),
        'IVA':       ('iva',       'IVA',                       [('Monto', 'numero'), ('Porcentaje', 'numero')]),
    }

    def factorial(self, numero_a):
        # El factorial de un número negativo no existe.
        if numero_a < 0:
            raise ErrorFactorialNegativo()

        # El factorial solo está definido para enteros: 2.5! no existe.
        if not float(numero_a).is_integer():
            raise ErrorFactorialNoEntero()

        # Casos base de la recursión: 0! = 1 y 1! = 1.
        if numero_a == 0 or numero_a == 1:
            return 1

        # RECURSIÓN: un método que se llama a sí mismo. El factorial
        # cumple la propiedad: n! = n * (n-1)!
        #   Ejemplo: 5! = 5 * 4! = 5 * 4 * 3! = ... = 5 * 4 * 3 * 2 * 1
        return numero_a * self.factorial(numero_a - 1)

    def mcm(self, numero_a, numero_b):
        for numero in (numero_a, numero_b):
            if not _es_entero_positivo(numero):
                raise ErrorEntradaNoValida("El MCM solo está definido para enteros positivos.")

        # Fórmula: MCM(a, b) = a * b / MCD(a, b)
        #   Ejemplo: MCM(12, 18) = 12 * 18 / MCD(12, 18) = 216 / 6 = 36
        # Reutilizamos el propio método mcd() de esta misma clase.
        mcd = self.mcd(numero_a, numero_b)
        return numero_a * numero_b // mcd

    def mcd(self, numero_a, numero_b):
        for numero in (numero_a, numero_b):
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
        a, b = numero_a, numero_b
        while b != 0:
            a, b = b, a % b
        return a

    def fibonacci(self, numero):
        n = numero

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
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b

        return b

    def iva(self, monto, porcentaje):
        # IVA = Impuesto de Valor Agregado: el porcentaje que se le suma
        # al precio de un producto. Regla de tres: el "porcentaje de
        # algo" = monto * porcentaje / 100.
        # Ejemplo: 100 pesos con IVA del 19% -> 100 * 19 / 100 = 19.
        return monto * porcentaje / 100