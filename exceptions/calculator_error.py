# Errores de Calculadora Personalizados (Para atrapar excepciones cómodamente ) - Kevin Gámez
"""Excepciones personalizadas usadas en todo el proyecto de la calculadora.

Usar una clase base común `ErrorCalculadora` permite que la capa de
interfaces atrape todos los errores de la calculadora con un único
`except`, mientras que aún permite manejar cada tipo de error de
forma específica cuando sea necesario.
"""

class ErrorCalculadora(Exception):
    """Clase base para las excepciones de esta calculadora."""
    def __init__(self, mensaje="Error en la calculadora."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorEntradaNoValida(ErrorCalculadora):
    """Excepción lanzada para entradas no válidas (MCM, MCD, etc.)."""
    def __init__(self, mensaje="Entrada no válida."):
        super().__init__(mensaje)

class ErrorOperacionDesconocida(ErrorCalculadora):
    """Excepción lanzada para operaciones desconocidas."""
    def __init__(self, mensaje="Operación desconocida."):
        super().__init__(mensaje)

class ErrorNumeroArgumentos(ErrorCalculadora):
    """Excepción lanzada cuando el número de argumentos es incorrecto."""
    def __init__(self, mensaje="Número incorrecto de argumentos."):
        super().__init__(mensaje)

class ErrorDivisionPorCero(ErrorCalculadora):
    """Excepción lanzada para errores de división por cero."""
    def __init__(self, mensaje="No se permite la división por cero."):
        super().__init__(mensaje)

class ErrorTangenteNoDefinida(ErrorCalculadora):
    """Excepción lanzada para valores de tangente no definidos."""
    def __init__(self, mensaje="La tangente no está definida para esta entrada."):
        super().__init__(mensaje)

class ErrorUnidadInvalida(ErrorCalculadora):
    """Excepción lanzada cuando la unidad del ángulo no es válida."""
    def __init__(self, mensaje="Unidad de ángulo no válida. Usa 'radianes' o 'grados'."):
        super().__init__(mensaje)

class ErrorFactorialNegativo(ErrorCalculadora):
    """Excepción lanzada para entradas de factorial negativas."""
    def __init__(self, mensaje="El factorial no está definido para números negativos."):
        super().__init__(mensaje)

class ErrorFactorialNoEntero(ErrorCalculadora):
    """Excepción lanzada para entradas de factorial no enteras."""
    def __init__(self, mensaje="El factorial solo está definido para números enteros."):
        super().__init__(mensaje)

class ErrorFibonacciNegativo(ErrorCalculadora):
    """Excepción lanzada para entradas de Fibonacci negativas."""
    def __init__(self, mensaje="El fibonacci no está definido para números negativos."):
        super().__init__(mensaje)

class ErrorNumeroImaginario(ErrorCalculadora):
    """Excepción lanzada para operaciones que resultan en números imaginarios."""
    def __init__(self, mensaje="La operación resultó en un número imaginario."):
        super().__init__(mensaje)

class ErrorPotenciaIndefinida(ErrorCalculadora):
    """Excepción lanzada cuando una potencia es indefinida."""
    def __init__(self, mensaje="La potencia está indefinida para esta operación."):
        super().__init__(mensaje)
