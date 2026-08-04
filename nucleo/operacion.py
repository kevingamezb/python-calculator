# Clase 'Padre' de Operación - Kevin Gámez

from abc import ABC, abstractmethod

class Operacion(ABC):

    # Cada subclase declara aquí las entradas que necesita, como lista
    # de tuplas (etiqueta, tipo). tipo puede ser 'numero' o 'unidad'.
    # La interfaz de consola las pide automáticamente leyendo este
    # atributo, así no hace falta tocar la consola al registrar nuevas
    # operaciones.
    entradas = []

    @abstractmethod
    def ejecutar(self):
        pass

    def __call__ (self):
        return self.ejecutar()
