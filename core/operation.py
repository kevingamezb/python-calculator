# Clase 'Padre' de Operación - Kevin Gámez

from abc import ABC, abstractmethod

class Operation(ABC):

    @abstractmethod
    def execute(self):
        pass

    def __call__ (self):
        return self.execute()