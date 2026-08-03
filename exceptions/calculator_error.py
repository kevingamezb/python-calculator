# Errores de Calculadora Personalizados (Para atrapar excepciones cómodamente ) - Kevin Gámez
"""Excepciones personalizadas usadas en todo el proyecto de la calculadora.

Usar una clase base común `CalculatorError` permite que la capa de
interfaces atrape todos los errores de la calculadora con un único
`except`, mientras que aún permite manejar cada tipo de error de
forma específica cuando sea necesario.
"""

class CalculatorError(Exception):
    """Clase base para las excepciones de esta calculadora."""
    pass

class InvalidInputError(CalculatorError):
    """Excepción lanzada para entradas no válidas."""
    pass

class UnknownOperationError(CalculatorError):
    """Excepción lanzada para operaciones desconocidas."""
    def __init__(self, message="Unknown operation provided."):
        self.message = message
        super().__init__(self.message)

class DivisionByZeroError(CalculatorError):
    """Excepción lanzada para errores de división por cero."""
    def __init__(self, message="Division by zero is not allowed."):
        self.message = message
        super().__init__(self.message)
        
class UndefinedTangentError(CalculatorError):
    """Excepción lanzada para valores de tangente no definidos."""
    def __init__(self, message="Tangent is undefined for this input."):
        self.message = message
        super().__init__(self.message)
        
class NegativeFactorialError(CalculatorError):
    """Excepción lanzada para entradas de factorial negativas."""
    def __init__(self, message="Factorial is not defined for negative numbers."):
        self.message = message
        super().__init__(self.message)
        
class NegativeFibonacciError(CalculatorError):
    """Excepción lanzada para entradas de Fibonacci negativas."""
    def __init__(self, message="Fibonacci is not defined for negative numbers."):
        self.message = message
        super().__init__(self.message)
    
class ImaginaryNumberError(CalculatorError):
    """Excepción lanzada para operaciones que resultan en números imaginarios."""
    def __init__(self, message="Operation resulted in an imaginary number."):
        self.message = message
        super().__init__(self.message)

class LCMError(CalculatorError):
    """Excepción lanzada por errores al calcular el MCM."""
    def __init__(self, message="Error in calculating LCM."):
        self.message = message
        super().__init__(self.message)
        
class GCDError(CalculatorError):
    """Excepción lanzada por errores al calcular el MCD."""
    def __init__(self, message="Error in calculating GCD."):
        self.message = message
        super().__init__(self.message)
        
