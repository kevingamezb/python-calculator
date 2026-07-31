# Lógica Principal de la Calculadora - Alvaro Orjuela & Kevin Gámez
"""
Main entry point that ties together all Operation subclasses through
a registry, exposing a single `calculate` method to the interfaces layer.
"""

from exceptions.calculator_error import UnknownOperationError


# TODO: importar aquí todas las clases de operación
# una vez que terminen sus archivos, por ejemplo:
from operations.trigonometric import Sine, Cosine, Tangent
# from operations.arithmetic import Add, Subtract, Multiply, Divide
# from operations.discrete import Factorial, Fibonacci, LCM, GCD
# from operations.exponential import Power, Root
# from operations.taxes import Vat


class Calculator:
    """Routes operation requests to the correct Operation subclass
    using a registry built at construction time.
    """

    def __init__(self):
        # Registry: mapea el nombre de la operación (lo que el usuario
        # elige en el menú) a la CLASE (no instancia) correspondiente.
        # Se instancia cada vez en calculate(), porque cada operación
        # necesita datos distintos por cada uso.
        self._operations = {
            # TODO: completar con cada operación, ej:
             'sin': Sine,
             'cos': Cosine,
             'tan': Tangent,
            # 'add': Add,
            # ...
        }

    def calculate(self, operation_name, *args):
        """Execute the operation identified by `operation_name` with
        the given arguments.

        Args:
            operation_name (str): key registered in self._operations.
            *args: arguments forwarded to the operation's constructor.

        Returns:
            The numeric result of the operation.

        Raises:
            UnknownOperationError: if the operation name is unknown, or if
                the number of arguments doesn't match what the
                operation's constructor expects.
        """
        if operation_name not in self._operations:
            raise UnknownOperationError(f"Unknown operation: {operation_name}")

        operation_class = self._operations[operation_name]

        # Capturamos TypeError aquí porque es lo que Python lanza
        # automáticamente si faltan o sobran argumentos al construir
        # la operación — lo traducimos a nuestra propia jerarquía de
        # excepciones para mantener consistencia con el resto del sistema.
        try:
            operation = operation_class(*args)
        except TypeError as e:
            raise UnknownOperationError(
                f"Wrong number of arguments for '{operation_name}': {e}"
            )

        return operation()  # usa __call__, definido en Operation