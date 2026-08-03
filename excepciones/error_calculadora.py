# Errores de Calculadora Personalizados - Kevin Gámez
"""
Excepciones propias del proyecto.

La clase base `ErrorCalculadora` permite que cualquier interfaz
(consola, ventana gráfica) atrape TODOS los errores de la calculadora
con un único `except`. Si algún día se necesita tratar un error de
forma distinta, se puede capturar la subclase específica.
"""

class ErrorCalculadora(Exception):
    """Base de todos los errores de la calculadora."""

    # Mensaje que se muestra cuando nadie pasa uno personalizado.
    # Cada subclase define el suyo con la misma variable.
    mensaje_por_defecto = "Error en la calculadora."

    def __init__(self, mensaje=None):
        # Si quien lanzó el error no pasó mensaje, usamos el
        # mensaje_por_defecto de la clase concreta que se lanzó.
        self.mensaje = mensaje if mensaje is not None else self.mensaje_por_defecto
        super().__init__(self.mensaje)


# Los errores específicos solo definen su mensaje por defecto.
# Toda la lógica de guardar el mensaje vive una sola vez, en la base.
# Si un caso puntual necesita otro texto, se pasa el mensaje al lanzar:
#   raise ErrorDivisionPorCero("No se puede dividir 5 entre 0")

class ErrorEntradaNoValida(ErrorCalculadora):
    """Entradas inválidas: números que no corresponden, etc."""
    mensaje_por_defecto = "Entrada no válida."

class ErrorOperacionDesconocida(ErrorCalculadora):
    """Se pidió una operación que no está en el registro."""
    mensaje_por_defecto = "Operación desconocida."

class ErrorNumeroArgumentos(ErrorCalculadora):
    """Faltan o sobran argumentos al construir la operación."""
    mensaje_por_defecto = "Número incorrecto de argumentos."

class ErrorDivisionPorCero(ErrorCalculadora):
    """No se puede dividir entre cero."""
    mensaje_por_defecto = "No se permite la división por cero."

class ErrorTangenteNoDefinida(ErrorCalculadora):
    """La tangente no existe donde el coseno vale cero."""
    mensaje_por_defecto = "La tangente no está definida para esta entrada."

class ErrorUnidadInvalida(ErrorCalculadora):
    """La unidad del ángulo no es 'radianes' ni 'grados'."""
    mensaje_por_defecto = "Unidad de ángulo no válida. Usa 'radianes' o 'grados'."

class ErrorFactorialNegativo(ErrorCalculadora):
    """El factorial no existe para números negativos."""
    mensaje_por_defecto = "El factorial no está definido para números negativos."

class ErrorFactorialNoEntero(ErrorCalculadora):
    """El factorial solo existe para números enteros."""
    mensaje_por_defecto = "El factorial solo está definido para números enteros."

class ErrorFibonacciNegativo(ErrorCalculadora):
    """La sucesión de Fibonacci empieza en 0; no hay términos negativos."""
    mensaje_por_defecto = "El fibonacci no está definido para números negativos."

class ErrorNumeroImaginario(ErrorCalculadora):
    """El resultado sería un número imaginario (ej. raíz par de un negativo)."""
    mensaje_por_defecto = "La operación resultó en un número imaginario."

class ErrorPotenciaIndefinida(ErrorCalculadora):
    """Caso indefinido en una potencia (por ejemplo, 0 elevado a 0)."""
    mensaje_por_defecto = "La potencia está indefinida para esta operación."
