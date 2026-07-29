# Operaciones Tirgonométricas (Seno, Coseno, Tangente) - Kevin Gámez
"""
Trigonometric operations for the calculator: sine, cosine, and tangent.

Each class receives an angle (and optionally its unit) through the
constructor, following the `Operation` contract defined in core/operation.py.
"""

from math import sin, cos, tan, isclose, radians
from core.operation import Operation
from exceptions.calculator_error import UndefinedTangentError


def _degrees_to_radians(degrees):
    """Convert an angle in degrees to radians."""
    return radians(degrees)


class Sine(Operation):
    """
    Calculates the sine of a given angle.

    Args:
        angle (float): the angle value.
        unit (str): 'radians' (default) or 'degrees'.
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
    Calculates the cosine of a given angle.

    Args:
        angle (float): the angle value.
        unit (str): 'radians' (default) or 'degrees'.
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
    Calculates the tangent of a given angle.

    Args:
        angle (float): the angle value.
        unit (str): 'radians' (default) or 'degrees'.

    Raises:
        UndefinedTangentError: if cos(angle) is (close to) zero,
            since tangent is undefined at those points.
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

