from math import sin, cos, tan, isclose, radians
from core.operation import Operation
from exceptions.calculator_error import UndefinedTangentError

def _degrees_to_radians(degrees):
    """Converts degrees to radians."""
    return radians(degrees)

class sine(Operation):
    """Calculates the sine of a given angle."""
    def execute(self, x, unit='radians'):
        if unit == 'degrees':
            x = _degrees_to_radians(x)
        return sin(x)

class cosine(Operation):
    """Calculates the cosine of a given angle."""
    def execute(self, x, unit='radians'):
        if unit == 'degrees':
            x = _degrees_to_radians(x)
        return cos(x)

class tangent(Operation):
    """Calculates the tangent of a given angle."""
    def execute(self, x, unit='radians'):
        if unit == 'degrees':
            x = _degrees_to_radians(x)
        if isclose(cos(x), 0, abs_tol=1e-9):
            raise UndefinedTangentError()
        return tan(x)