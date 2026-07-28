from operations.arithmetic import Arithmetic
from operations.trigonometric import Trigonometric
from operations.taxes import Taxes
from operations.discrete import Discrete
from operations.exponential import Exponential

class Operation:
    """Class to 'wrap' all operations in the calculator."""
    def __init__(self):
        self.operations = {
            'add'      : Arithmetic.add(),
            'subtract' : Arithmetic.subtract(),
            'multiply' : Arithmetic.multiply(),
            'divide'   : Arithmetic.divide(),
            'sin'      : Trigonometric.sin(),
            'cos'      : Trigonometric.cos(),
            'tan'      : Trigonometric.tan(),
            'vat'      : Taxes.vat(),
            'factorial': Discrete.factorial(),
            'fibonacci': Discrete.fibonacci(),
            'lcm'      : Discrete.lcm(),
            'gcd'      : Discrete.gcd(),
            'power'    : Exponential.power(),
            'root'     : Exponential.root(),}
        
