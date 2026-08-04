# Operaciones de Impuestos (Impuesto de Valor Agregado) - Shalon León

from nucleo.operacion import Operacion

class IVA(Operacion):
    etiqueta = 'IVA'

    def __init__(self, monto, porcentaje):
        self._monto = monto
        self._porcentaje = porcentaje

    def ejecutar(self):
        return self._monto * self._porcentaje / 100
