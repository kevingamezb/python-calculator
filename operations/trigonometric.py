from math import sin, cos, tan, isclose, radians
from exceptions.calculator_error import UndefinedTangentError

class Trigonometric():
    """Class for trigonometric operations."""
    
    @staticmethod
    def _degrees_to_radians(degrees):
        """Convert degrees to radians."""
        return radians(degrees)
    
    @staticmethod
    def sin(x, unit='radians'):
        """Calculate the sine of x (in radians)."""
        if unit == 'degrees':
            x = Trigonometric._degrees_to_radians(x)
        return sin(x)
    
    @staticmethod
    def cos(x, unit='radians'):
        """Calculate the cosine of x (in radians)."""
        if unit == 'degrees':
            x = Trigonometric._degrees_to_radians(x)
        return cos(x)

    @staticmethod
    def tan(x, unit='radians'):
        """Calculate the tangent of x (in radians)."""
        if unit == 'degrees':
            x = Trigonometric._degrees_to_radians(x)
        if isclose(cos(x), 0, abs_tol=1e-9):
            raise UndefinedTangentError()
        return tan(x)
