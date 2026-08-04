# Operaciones de Impuestos (Impuesto de Valor Agregado) - Shalon León

from nucleo.operacion import Operacion

class IVA(Operacion):
    etiqueta = 'IVA'

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        multiplicacion = self._numero_a * self._numero_b
        iva = multiplicacion / 100
        return iva
