# Operaciones de Impuestos (Impuesto de Valor Agregado) - Shalon León
"""
IVA = Impuesto de Valor Agregado: el porcentaje que se le suma al precio
de un producto. Ejemplo: compras algo de 100 pesos con IVA del 19% ->
pagas 19 pesos de impuesto.

El constructor recibe DOS datos, y los nombres importan para saber cuál
es cuál: `monto` es la plata que gastaste y `porcentaje` es el porcentaje
de impuesto (ej. 19).
"""

from nucleo.operacion import Operacion

class IVA(Operacion):
    etiqueta = 'IVA'
    entradas = [('Monto', 'numero'), ('Porcentaje', 'numero')]

    def __init__(self, monto, porcentaje):
        self._monto = monto
        self._porcentaje = porcentaje

    def ejecutar(self):
        # Regla de tres: el "porcentaje de algo" = monto * porcentaje / 100.
        # Se divide entre 100 porque "19%" significa "19 de cada 100".
        # Ejemplo: 100 * 19 / 100 = 19.
        return self._monto * self._porcentaje / 100
