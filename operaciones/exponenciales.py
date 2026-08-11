# Operaciones Exponenciales (Potencia, Raíz) - Alvaro Orjuela
"""
Dos operaciones relacionadas: elevar a una potencia y sacar raíces.

Dato curioso: en matemáticas, la raíz n-ésima de un número es lo mismo
que elevarlo a 1/n. Por eso las dos se calculan con el mismo operador
** (potencia), que es el que usa Python.
"""

from excepciones.error_calculadora import ErrorEntradaNoValida, ErrorNumeroImaginario, ErrorPotenciaIndefinida


class Exponencial:

    OPERACIONES = {
        'Potencia': ('potencia', 'Potencia', [('Base', 'numero'), ('Exponente', 'numero')]),
        'Raiz':     ('raiz',     'Raíz',     [('Radicando', 'numero'), ('Índice', 'numero')]),
    }

    def potencia(self, base, exponente):
        # 0^0 (cero elevado a cero) es un caso indefinido en matemáticas:
        # no hay un resultado único, por eso lo tratamos como error.
        if base == 0 and exponente == 0:
            raise ErrorPotenciaIndefinida()

        # Un número negativo elevado a un exponente NO entero
        # (ej. (-8) ** 0.5) daría un número imaginario. Python sí sabe
        # calcularlo, pero nosotros preferimos avisar con nuestro error.
        if base < 0 and not float(exponente).is_integer():
            raise ErrorNumeroImaginario()

        # ** es el operador de potencia: 2 ** 10 = 1024.
        return base ** exponente

    def raiz(self, radicando, indice):
        # "Índice" es el numerito de la raíz: en la raíz cuadrada es 2,
        # en la cúbica es 3. No puede ser 0.
        if indice == 0:
            raise ErrorEntradaNoValida("El índice de la raíz no puede ser cero.")

        if radicando < 0:
            # Sacar la raíz de un número negativo depende del índice:
            #   - Índice IMPAR (raíz cúbica de -8): existe y da negativo (-2).
            #   - Índice PAR (raíz cuadrada de -8): no existe en los reales,
            #     sería un número imaginario.
            if float(indice).is_integer() and indice % 2 != 0:
                # Para la raíz impar de un negativo: convertimos el número
                # a positivo, sacamos la raíz y al final le ponemos el
                # signo menos. Ej: -((-8) ** (1/3)) = -(8 ** 0.333...) = -2.
                return -((-radicando) ** (1 / indice))
            # Índice par (o no entero): el resultado sería imaginario.
            raise ErrorNumeroImaginario()

        # Truco matemático: la raíz n-ésima de un número es lo mismo que
        # elevarlo a 1/n. Por eso "raíz cuadrada de 16" es 16 ** (1/2).
        return radicando ** (1 / indice)