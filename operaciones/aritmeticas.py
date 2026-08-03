# Operaciones Aritméticas (Suma, Resta, Multiplicación, División) - Shalon León
from nucleo.operacion import Operacion
from excepciones.error_calculadora import ErrorDivisionPorCero
class Division(Operacion):
    etiqueta = 'División'

    def __init__(self, numero_a, numero_b):
            self._numero_a = numero_a
            self._numero_b = numero_b

    def ejecutar(self):
            if self._numero_b == 0:
                raise ErrorDivisionPorCero()
            return self._numero_a / self._numero_b
"""
Pasos para crear una operación:
1. Heredar de `Operacion` (nucleo/operacion.py).
2. Definir `etiqueta`: es el nombre que la interfaz mostrará en el menú.
3. Guardar los datos en atributos con guion bajo (`self._...`). El guion
   bajo es una convención que avisa "no toques esto desde fuera"; NO es
   una protección real como `private` en C++.
4. Implementar `ejecutar()` con la lógica y devolver el resultado.

Los errores propios de la calculadora (como dividir por cero) se lanzan
con las excepciones de excepciones/error_calculadora.py.

Cuando la operación esté lista, se importa y se registra en
nucleo/calculadora.py; el menú de la consola la incluye automáticamente.
"""
