# Operaciones Exponenciales (Potencia, Raíz) - Alvaro Orjuela

#def _es_par(numero):




from nucleo.operacion import Operacion

class Potencia(Operacion):
    etiqueta = 'Potencia'

    def __init__(self, base, exponente):
        self._base = base
        self._exponente = exponente

    def ejecutar(self):
        return self._base ** self._exponente


class Raiz(Operacion):
    etiqueta = 'Raíz'

    def __init__(self, radicando, indice):
        self._radicando = radicando
        self._indice = indice

    def ejecutar(self):
        return self._radicando ** (1/self._indice)