# Operaciones Exponenciales (Potencia, Raíz) - Alvaro Orjuela

from nucleo.operacion import Operacion
from excepciones.error_calculadora import ErrorEntradaNoValida, ErrorNumeroImaginario, ErrorPotenciaIndefinida


class Potencia(Operacion):
    etiqueta = 'Potencia'
    entradas = [('Base', 'numero'), ('Exponente', 'numero')]

    def __init__(self, base, exponente):
        self._base = base
        self._exponente = exponente

    def ejecutar(self):
        if self._base == 0 and self._exponente == 0:
            raise ErrorPotenciaIndefinida()

        if self._base < 0 and not float(self._exponente).is_integer():
            raise ErrorNumeroImaginario()

        return self._base ** self._exponente


class Raiz(Operacion):
    etiqueta = 'Raíz'
    entradas = [('Radicando', 'numero'), ('Índice', 'numero')]

    def __init__(self, radicando, indice):
        self._radicando = radicando
        self._indice = indice

    def ejecutar(self):
        if self._indice == 0:
            raise ErrorEntradaNoValida("El índice de la raíz no puede ser cero.")

        if self._radicando < 0:
            # Índice impar: la raíz de un negativo es real y negativa.
            if float(self._indice).is_integer() and self._indice % 2 != 0:
                return -((-self._radicando) ** (1 / self._indice))
            # Índice par (o no entero): el resultado sería imaginario.
            raise ErrorNumeroImaginario()

        return self._radicando ** (1 / self._indice)
