# Clase 'Padre' de Operación - Kevin Gámez

from abc import ABC, abstractmethod

class Operacion(ABC):

    @abstractmethod
    def ejecutar(self):
        pass

    def __call__ (self):
        return self.ejecutar()
