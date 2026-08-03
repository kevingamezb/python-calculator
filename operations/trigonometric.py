# Operaciones Trigonométricas (Seno, Coseno, Tangente) - Kevin Gámez
"""
Operaciones trigonométricas para la calculadora: seno, coseno y tangente.

Cada clase recibe un ángulo (y opcionalmente su unidad) a través del
constructor, siguiendo el contrato de `Operacion` definido en core/operation.py.
"""

from math import sin, cos, tan, isclose, radians
from core.operation import Operacion
from exceptions.calculator_error import ErrorTangenteNoDefinida, ErrorUnidadInvalida

_UNIDADES_VALIDAS = ('radianes', 'grados')


def _grados_a_radianes(grados):
    """Convierte un ángulo en grados a radianes."""
    return radians(grados)


class Seno(Operacion):
    """
    Calcula el seno de un ángulo dado.

    Argumentos:
        angulo (float): el valor del ángulo.
        unidad (str): 'radianes' (por defecto) o 'grados'.

    Lanza:
        ErrorUnidadInvalida: si la unidad no es 'radianes' ni 'grados'.
    """
    def __init__(self, angulo, unidad='radianes'):
        if unidad not in _UNIDADES_VALIDAS:
            raise ErrorUnidadInvalida()
        self._angulo = angulo
        self._unidad = unidad

    def ejecutar(self):
        angulo = self._angulo
        # Usamos una variable local para no modificar self._angulo:
        # así ejecutar() siempre da el mismo resultado sin importar
        # cuántas veces se llame sobre el mismo objeto.
        if self._unidad == 'grados':
            angulo = _grados_a_radianes(angulo)
        return sin(angulo)


class Coseno(Operacion):
    """
    Calcula el coseno de un ángulo dado.

    Argumentos:
        angulo (float): el valor del ángulo.
        unidad (str): 'radianes' (por defecto) o 'grados'.

    Lanza:
        ErrorUnidadInvalida: si la unidad no es 'radianes' ni 'grados'.
    """
    def __init__(self, angulo, unidad='radianes'):
        if unidad not in _UNIDADES_VALIDAS:
            raise ErrorUnidadInvalida()
        self._angulo = angulo
        self._unidad = unidad

    def ejecutar(self):
        angulo = self._angulo
        if self._unidad == 'grados':
            angulo = _grados_a_radianes(angulo)
        return cos(angulo)


class Tangente(Operacion):
    """
    Calcula la tangente de un ángulo dado.

    Argumentos:
        angulo (float): el valor del ángulo.
        unidad (str): 'radianes' (por defecto) o 'grados'.

    Lanza:
        ErrorUnidadInvalida: si la unidad no es 'radianes' ni 'grados'.
        ErrorTangenteNoDefinida: si cos(angulo) es (cercano a) cero,
            ya que la tangente no está definida en esos puntos.
    """
    def __init__(self, angulo, unidad='radianes'):
        if unidad not in _UNIDADES_VALIDAS:
            raise ErrorUnidadInvalida()
        self._angulo = angulo
        self._unidad = unidad

    def ejecutar(self):
        angulo = self._angulo
        if self._unidad == 'grados':
            angulo = _grados_a_radianes(angulo)
        # isclose() en vez de == 0: por errores de precisión de punto
        # flotante, cos(x) casi nunca da exactamente 0 aunque
        # matemáticamente debería. abs_tol define qué tan "cerca" de
        # cero se considera indefinido.
        if isclose(cos(angulo), 0, abs_tol=1e-9):
            raise ErrorTangenteNoDefinida()
        return tan(angulo)
