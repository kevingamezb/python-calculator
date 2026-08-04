# Operaciones Trigonométricas (Seno, Coseno, Tangente) - Kevin Gámez
"""
Seno, coseno y tangente para la calculadora.

Las tres reciben un ángulo y (opcionalmente) su unidad. La clase base
`OperacionAngular` hace el trabajo común: valida la unidad y convierte
a radianes, para no repetir ese código en cada operación.
"""
from abc import ABC
from math import sin, cos, tan, isclose, radians
from nucleo.operacion import Operacion
from excepciones.error_calculadora import ErrorTangenteNoDefinida, ErrorUnidadInvalida

# Unidades aceptadas. Se comparan en minúsculas, por eso normalizamos
# con .lower() al construir la operación: así 'grados', 'GRADOS' o
# 'Grados' valen lo mismo.
_UNIDADES_VALIDAS = ('radianes', 'grados')


class OperacionAngular(Operacion, ABC):
    """Base para operaciones que reciben un ángulo y su unidad."""

    # La consola pide el ángulo y la unidad en este mismo orden.
    entradas = [('Ángulo', 'numero'), ('Unidad', 'unidad')]

    def __init__(self, angulo, unidad='radianes'):
        # Normalizamos la unidad a minúsculas. Si no es un texto, la
        # dejamos vacía para que falle la validación de abajo.
        unidad = unidad.lower() if isinstance(unidad, str) else ''
        if unidad not in _UNIDADES_VALIDAS:
            raise ErrorUnidadInvalida()
        self._angulo = angulo
        self._unidad = unidad

    def _angulo_en_radianes(self):
        """
        Devuelve el ángulo convertido a radianes.

        Usamos una variable local para no modificar self._angulo:
        así ejecutar() siempre da el mismo resultado aunque se llame
        varias veces sobre el mismo objeto.
        """
        angulo = self._angulo
        if self._unidad == 'grados':
            angulo = radians(angulo)
        return angulo


class Seno(OperacionAngular):
    """Calcula el seno del ángulo."""
    etiqueta = 'Seno'

    def ejecutar(self):
        return sin(self._angulo_en_radianes())


class Coseno(OperacionAngular):
    """Calcula el coseno del ángulo."""
    etiqueta = 'Coseno'

    def ejecutar(self):
        return cos(self._angulo_en_radianes())


class Tangente(OperacionAngular):
    """Calcula la tangente del ángulo."""
    etiqueta = 'Tangente'

    def ejecutar(self):
        angulo = self._angulo_en_radianes()
        # isclose() en vez de == 0: por errores de precisión de punto
        # flotante, cos(x) casi nunca da exactamente 0 aunque
        # matemáticamente debería. abs_tol define qué tan "cerca" de
        # cero se considera indefinido.
        if isclose(cos(angulo), 0, abs_tol=1e-9):
            raise ErrorTangenteNoDefinida()
        return tan(angulo)
