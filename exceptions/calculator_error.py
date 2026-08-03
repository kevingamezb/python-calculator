# Errores de Calculadora Personalizados (Para atrapar excepciones cómodamente ) - Kevin Gámez
"""Excepciones personalizadas usadas en todo el proyecto de la calculadora.

Usar una clase base común `ErrorCalculadora` permite que la capa de
interfaces atrape todos los errores de la calculadora con un único
`except`, mientras que aún permite manejar cada tipo de error de
forma específica cuando sea necesario.
"""

class ErrorCalculadora(Exception):
    """Clase base para las excepciones de esta calculadora."""
    pass

class ErrorEntradaNoValida(ErrorCalculadora):
    """Excepción lanzada para entradas no válidas."""
    pass

class ErrorOperacionDesconocida(ErrorCalculadora):
    """Excepción lanzada para operaciones desconocidas."""
    def __init__(self, mensaje="Operación desconocida."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorDivisionPorCero(ErrorCalculadora):
    """Excepción lanzada para errores de división por cero."""
    def __init__(self, mensaje="No se permite la división por cero."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        
class ErrorTangenteNoDefinida(ErrorCalculadora):
    """Excepción lanzada para valores de tangente no definidos."""
    def __init__(self, mensaje="La tangente no está definida para esta entrada."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        
class ErrorFactorialNegativo(ErrorCalculadora):
    """Excepción lanzada para entradas de factorial negativas."""
    def __init__(self, mensaje="El factorial no está definido para números negativos."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        
class ErrorFibonacciNegativo(ErrorCalculadora):
    """Excepción lanzada para entradas de Fibonacci negativas."""
    def __init__(self, mensaje="El fibonacci no está definido para números negativos."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
    
class ErrorNumeroImaginario(ErrorCalculadora):
    """Excepción lanzada para operaciones que resultan en números imaginarios."""
    def __init__(self, mensaje="La operación resultó en un número imaginario."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorMCM(ErrorCalculadora):
    """Excepción lanzada por errores al calcular el MCM."""
    def __init__(self, mensaje="Error al calcular el MCM."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        
class ErrorMCD(ErrorCalculadora):
    """Excepción lanzada por errores al calcular el MCD."""
    def __init__(self, mensaje="Error al calcular el MCD."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        
