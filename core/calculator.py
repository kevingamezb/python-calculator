# Lógica Principal de la Calculadora - Alvaro Orjuela & Kevin Gámez
"""
Punto de entrada principal que conecta todas las subclases de `Operation`
a través de un registro, exponiendo un único método `calculate` a la
capa de interfaces.
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
    """Enruta las solicitudes de operación hacia la subclase de `Operation`
    correcta, usando un registro construido al momento de la creación.
    """

    def __init__(self):
        # Registro: mapea el nombre de la operación (lo que el usuario
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
        """Ejecuta la operación identificada por `operation_name` con los
        argumentos dados.

        Argumentos:
            operation_name (str): clave registrada en self._operations.
            *args: argumentos que se pasan al constructor de la operación.

        Retorna:
            El resultado numérico de la operación.

        Lanza:
            UnknownOperationError: si el nombre de la operación es desconocido,
                o si el número de argumentos no coincide con lo que el
                constructor de la operación espera.
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
