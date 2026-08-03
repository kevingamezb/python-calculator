# Lógica Principal de la Calculadora - Alvaro Orjuela & Kevin Gámez
"""
Punto de entrada principal que conecta todas las subclases de `Operacion`
a través de un registro, exponiendo un único método `calcular` a la
capa de interfaces.
"""

from exceptions.calculator_error import ErrorNumeroArgumentos, ErrorOperacionDesconocida


# TODO: importar aquí todas las clases de operación
# una vez que terminen sus archivos, por ejemplo:
from operations.trigonometric import Seno, Coseno, Tangente
# from operations.arithmetic import Suma, Resta, Multiplicacion, Division
# from operations.discrete import Factorial, Fibonacci, MCM, MCD
# from operations.exponential import Potencia, Raiz
# from operations.taxes import Iva


class Calculadora:
    """Enruta las solicitudes de operación hacia la subclase de `Operacion`
    correcta, usando un registro construido al momento de la creación.
    """

    def __init__(self):
        # Registro: mapea el nombre de la operación (lo que el usuario
        # elige en el menú) a la CLASE (no instancia) correspondiente.
        # Se instancia cada vez en calcular(), porque cada operación
        # necesita datos distintos por cada uso.
        self._operaciones = {
            # TODO: completar con cada operación, ej:
             'sen': Seno,
             'cos': Coseno,
             'tan': Tangente,
            # 'suma': Suma,
            # ...
        }

    def calcular(self, nombre_operacion, *args):
        """Ejecuta la operación identificada por `nombre_operacion` con los
        argumentos dados.

        Argumentos:
            nombre_operacion (str): clave registrada en self._operaciones.
            *args: argumentos que se pasan al constructor de la operación.

        Retorna:
            El resultado numérico de la operación.

        Lanza:
            ErrorOperacionDesconocida: si el nombre de la operación es desconocido.
            ErrorNumeroArgumentos: si el número de argumentos no coincide con lo
                que el constructor de la operación espera.
        """
        if nombre_operacion not in self._operaciones:
            raise ErrorOperacionDesconocida(f"Operación desconocida: {nombre_operacion}")

        clase_operacion = self._operaciones[nombre_operacion]

        # Capturamos TypeError aquí porque es lo que Python lanza
        # automáticamente si faltan o sobran argumentos al construir
        # la operación — lo traducimos a nuestra propia jerarquía de
        # excepciones para mantener consistencia con el resto del sistema.
        try:
            operacion = clase_operacion(*args)
        except TypeError as e:
            raise ErrorNumeroArgumentos(
                f"Número incorrecto de argumentos para '{nombre_operacion}': {e}"
            )

        return operacion()  # usa __call__, definido en Operacion
