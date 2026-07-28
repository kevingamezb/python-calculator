# Calculator Errors - Kevin Gámez

class CalculatorError(Exception):
    """Base class for exceptions in this calculator."""
    pass

class InvalidInputError(CalculatorError):
    """Exception raised for invalid inputs."""
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)

class DivisionByZeroError(CalculatorError):
    """Exception raised for division by zero errors."""
    def __init__(self, message="Division by zero is not allowed."):
        self.message = message
        super().__init__(self.message)
        
class UndefinedTangentError(CalculatorError):
    """Exception raised for undefined tangent values."""
    def __init__(self, message="Tangent is undefined for this input."):
        self.message = message
        super().__init__(self.message)
        
class NegativeFactorialError(CalculatorError):
    """Exception raised for negative factorial inputs."""
    def __init__(self, message="Factorial is not defined for negative numbers."):
        self.message = message
        super().__init__(self.message)
        
class NegativeFibonacciError(CalculatorError):
    """Exception raised for negative Fibonacci inputs."""
    def __init__(self, message="Fibonacci is not defined for negative numbers."):
        self.message = message
        super().__init__(self.message)
    
class ImaginaryNumberError(CalculatorError):
    """Exception raised for operations resulting in imaginary numbers."""
    def __init__(self, message="Operation resulted in an imaginary number."):
        self.message = message
        super().__init__(self.message)

class LCMError(CalculatorError):
    """Exception raised for errors in calculating LCM."""
    def __init__(self, message="Error in calculating LCM."):
        self.message = message
        super().__init__(self.message)
        
class GCDError(CalculatorError):
    """Exception raised for errors in calculating GCD."""
    def __init__(self, message="Error in calculating GCD."):
        self.message = message
        super().__init__(self.message)
        
