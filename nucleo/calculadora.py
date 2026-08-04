# Lógica Principal de la Calculadora - Alvaro Orjuela & Kevin Gámez
"""
Punto de entrada principal que conecta todas las subclases de `Operacion`
a través de un registro, exponiendo una única función `calcular` a la
capa de interfaces.
"""

from excepciones.error_calculadora import ErrorNumeroArgumentos, ErrorOperacionDesconocida
# TODO: importar aquí todas las clases de operación
# una vez que terminen sus archivos, por ejemplo:
from operaciones.trigonometricas import Seno, Coseno, Tangente
from operaciones.aritmeticas import Suma, Resta, Multiplicacion, Division
# from operaciones.discretas import Factorial, Fibonacci, MCM, MCD
# from operaciones.exponenciales import Potencia, Raiz
from operaciones.impuestos import IVA


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
            'Suma'          :  Suma,
            'Resta'         :  Resta,
            'Multiplicacion':  Multiplicacion,
            'Division'      :  Division,
            'sen'           :  Seno,
            'cos'           :  Coseno,
            'tan'           :  Tangente,
            'IVA': IVA,
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

    def operaciones_disponibles(self):
        """Devuelve el registro de operaciones disponibles como una lista
        de tuplas (nombre_operacion, etiqueta), en el orden en que fueron
        registradas.

        Se apoya en el atributo de clase `etiqueta` que cada subclase de
        `Operacion` debe definir (ver operaciones/trigonometricas.py para
        un ejemplo). Así, la interfaz de consola (u otra) puede construir
        su menú automáticamente a partir de self._operaciones, sin
        necesidad de mantener una lista aparte sincronizada a mano.
        """
        return [
            (nombre, clase_operacion.etiqueta)
            for nombre, clase_operacion in self._operaciones.items()
        ]