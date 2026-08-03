# Operaciones Aritméticas (Suma, Resta, Multiplicación, División) - Shalon León
from exceptions.calculator_error import ErrorDivisionPorCero

#class Division(Operacion): // Herencia de `Operacion`
#   def __init__(self, numero_a, numero_b): // Constructor
#       self._numero_a = numero_a // Se usa '_' para marcar un 'encapsulamiento semántico'
#       self._numero_b = numero_b // Esto no protege realmente como `private` en C++
#
#   def ejecutar(self): // Polimorfismo de la función `ejecutar()` de `Operacion`
#       dividendo = self._numero_a // Usamos variables locales para no modificar `self.(...)` por error
#       divisor = self._numero_b
#       try:
#           return dividendo / divisor
#       except Exception:
#           raise ErrorDivisionPorCero()
