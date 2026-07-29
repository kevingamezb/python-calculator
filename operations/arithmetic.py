# Arithmetic Operations (Add, Substract, Multiply, Divide) - Shalon León
from exceptions.calculator_error import DivisionByZeroError

#class Divide(Operation): // Herencia de `Operation`
#   def __init__(self, a, b): // Constructor
#       self._a = a // Se usa '_' para marcar un 'encapsulamiento semántico'
#       self._b = b // Esto no protege realmente como `private` en C++
#
#   def execute(self): // Polimorfismo de la función `execute()` de `Operation`
#       dividend = self._a // Usamos variable locales para no modificar `self.(...)` por error
#       divisor = self._b
#       try:
#           return dividend / divisor
#       except Exception:
#           raise DivisionByZeroError()