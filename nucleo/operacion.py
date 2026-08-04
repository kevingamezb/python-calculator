# Clase 'Padre' de Operación - Kevin Gámez

# ABC = Abstract Base Class (Clase Base Abstracta). Importamos la clase y
# el decorador abstractmethod para poder "obligar" a las subclases a
# implementar el método ejecutar().
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
        # Este método NO tiene cuerpo (solo 'pass'): cada operación
        # concreta (Suma, Seno, Factorial...) implementa aquí CÓMO se
        # calcula. El decorador @abstractmethod hace que NO se pueda
        # crear un objeto Operacion directamente, y que toda subclase
        # esté obligada a escribir su propio ejecutar(). Si una subclase
        # no lo hace, Python lanza TypeError al intentar instanciarla.
        pass

    def __call__(self):
        # Los métodos "dunder" (de doble guion bajo) le dan significado
        # a los operadores de Python. __call__ es el que se ejecuta
        # cuando llamas al objeto como si fuera una función:
        #
        #   operacion = Suma(5, 3)   # crea el objeto
        #   operacion()              # Python ejecuta operacion.__call__()
        #
        # Definirlo aquí (una sola vez) hace que TODAS las operaciones
        # se puedan ejecutar igual con los paréntesis, sin tener que
        # repetir este método en cada una.
        return self.ejecutar()
