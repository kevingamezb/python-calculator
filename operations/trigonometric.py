from math import sin, cos, tan, isclose, radians
from core.operation import Operation
from exceptions.calculator_error import UndefinedTangentError

def _degrees_to_radians(degrees):
    """Converts degrees to radians."""
    return radians(degrees)

class Sine(Operation):
    """Calculates the sine of a given angle."""
    def __init__(self, angle, unit='radians'):
        self.angle = angle
        self.unit = unit

    def execute(self):
        angle = self.angle

        if self.unit == 'degrees':
            angle = _degrees_to_radians(angle)
        return sin(angle)

class Cosine(Operation):
    """Calculates the cosine of a given angle."""
    def __init__(self, angle, unit='radians'):
        self.angle = angle
        self.unit = unit

    def execute(self):
        angle = self.angle

        if self.unit == 'degrees':
            angle = _degrees_to_radians(angle)
        return cos(angle)

class Tangent(Operation):
    """Calculates the tangent of a given angle."""
    def __init__(self, angle, unit='radians'):
        self.angle = angle
        self.unit = unit

    def execute(self):
        angle = self.angle

        if self.unit == 'degrees':
            angle = _degrees_to_radians(angle)
        if isclose(cos(angle), 0, abs_tol=1e-9):
            raise UndefinedTangentError()
        return tan(angle)