# Operaciones Tirgonométricas (Seno, Coseno, Tangente) - Kevin Gámez
"""
Operaciones trigonométricas para la calculadora: seno, coseno y tangente.

Cada clase recibe un ángulo (y opcionalmente su unidad) a través del
constructor, siguiendo el contrato de `Operation` definido en core/operation.py.
"""

from math import sin, cos, tan, isclose, radians
from core.operation import Operation
from exceptions.calculator_error import UndefinedTangentError


def _degrees_to_radians(degrees):
    """Convierte un ángulo en grados a radianes."""
    return radians(degrees)


class Sine(Operation):
    """
    Calcula el seno de un ángulo dado.

    Argumentos:
        angle (float): el valor del ángulo.
        unit (str): 'radians' (por defecto) o 'degrees'.
    """
    def __init__(self, angle, unit='radians'):
        self._angle = angle
        self._unit = unit

    def execute(self):
        angle = self._angle
        # Usamos una variable local para no modificar self.angle:
        # así execute() siempre da el mismo resultado sin importar
        # cuántas veces se llame sobre el mismo objeto.
        if self._unit == 'degrees':
            angle = _degrees_to_radians(angle)
        return sin(angle)


class Cosine(Operation):
    """
    Calcula el coseno de un ángulo dado.

    Argumentos:
        angle (float): el valor del ángulo.
        unit (str): 'radians' (por defecto) o 'degrees'.
    """
    def __init__(self, angle, unit='radians'):
        self._angle = angle
        self._unit = unit

    def execute(self):
        angle = self._angle
        if self._unit == 'degrees':
            angle = _degrees_to_radians(angle)
        return cos(angle)


class Tangent(Operation):
    """
    Calcula la tangente de un ángulo dado.

    Argumentos:
        angle (float): el valor del ángulo.
        unit (str): 'radians' (por defecto) o 'degrees'.

    Lanza:
        UndefinedTangentError: si cos(angle) es (cercano a) cero,
            ya que la tangente no está definida en esos puntos.
    """
    def __init__(self, angle, unit='radians'):
        self._angle = angle
        self._unit = unit

    def execute(self):
        angle = self._angle
        if self._unit == 'degrees':
            angle = _degrees_to_radians(angle)
        # isclose() en vez de == 0: por errores de precisión de punto
        # flotante, cos(x) casi nunca da exactamente 0 aunque
        # matemáticamente debería. abs_tol define qué tan "cerca" de
        # cero se considera indefinido.
        if isclose(cos(angle), 0, abs_tol=1e-9):
            raise UndefinedTangentError()
        return tan(angle)
