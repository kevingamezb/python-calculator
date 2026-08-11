# Operaciones Trigonométricas (Seno, Coseno, Tangente) - Kevin Gámez
"""
Seno, coseno y tangente para la calculadora.

Las tres reciben un ángulo y (opcionalmente) su unidad. El método
privado `_angulo_en_radianes` hace el trabajo común: valida la unidad
y convierte a radianes, para no repetir ese código en cada operación
(antes esto vivía en una clase base `OperacionAngular` compartida
entre 3 clases; ahora es un método privado dentro de la única clase
`Trigonometrica`).
"""

from math import sin, cos, tan, isclose, radians
from excepciones.error_calculadora import ErrorTangenteNoDefinida, ErrorUnidadInvalida

# Unidades aceptadas. Se comparan en minúsculas, por eso normalizamos
# con .lower() antes de validar: así 'grados', 'GRADOS' o 'Grados'
# valen lo mismo.
_UNIDADES_VALIDAS = ('radianes', 'grados')

_ENTRADAS_ANGULO = [('Ángulo', 'numero'), ('Unidad', 'unidad')]


class Trigonometrica:

    OPERACIONES = {
        'sen': ('seno',     'Seno',     _ENTRADAS_ANGULO),
        'cos': ('coseno',   'Coseno',   _ENTRADAS_ANGULO),
        'tan': ('tangente', 'Tangente', _ENTRADAS_ANGULO),
    }

    def _angulo_en_radianes(self, angulo, unidad):
        """
        Devuelve el ángulo convertido a radianes, validando primero
        que la unidad recibida sea 'radianes' o 'grados'.
        """
        unidad = unidad.lower() if isinstance(unidad, str) else ''
        if unidad not in _UNIDADES_VALIDAS:
            raise ErrorUnidadInvalida()
        if unidad == 'grados':
            angulo = radians(angulo)
        return angulo

    def seno(self, angulo, unidad='radianes'):
        return sin(self._angulo_en_radianes(angulo, unidad))

    def coseno(self, angulo, unidad='radianes'):
        return cos(self._angulo_en_radianes(angulo, unidad))

    def tangente(self, angulo, unidad='radianes'):
        angulo_rad = self._angulo_en_radianes(angulo, unidad)
        # isclose() en vez de == 0: por errores de precisión de punto
        # flotante, cos(x) casi nunca da exactamente 0 aunque
        # matemáticamente debería. abs_tol define qué tan "cerca" de
        # cero se considera indefinido.
        if isclose(cos(angulo_rad), 0, abs_tol=1e-9):
            raise ErrorTangenteNoDefinida()
        return tan(angulo_rad)