# Registro de Operaciones - Kevin Gámez
"""
Antes, cada operación (Suma, Seno, Factorial...) era su propia clase,
obligada por `Operacion(ABC)` a implementar `ejecutar()`. Ahora solo
hay 4 clases (una por categoría: Aritmetica, Discreta, Exponencial,
Trigonometrica) y cada operación es un MÉTODO dentro de su categoría.

El "contrato" que antes vivía en la clase (etiqueta, entradas) ahora
vive en `OperacionRegistrada`: un envoltorio liviano que guarda esos
mismos dos datos más el método ya "ligado" (bound method) a la
instancia de su categoría, listo para llamarse con `operacion(*args)`.

Cada clase categoría declara un diccionario de clase `OPERACIONES` con
esta forma:

    OPERACIONES = {
        'Suma': ('sumar', 'Suma', [('Primer número', 'numero'), ('Segundo número', 'numero')]),
        #  ^clave para el registro   ^nombre del método   ^etiqueta   ^entradas (igual que antes)
    }

`nucleo/calculadora.py` recorre las 4 categorías, lee sus `OPERACIONES`
y arma un `OperacionRegistrada` por cada una. Así, `interfaces/consola.py`
no cambia casi nada: sigue leyendo `.entradas` y `.etiqueta` igual que
cuando esos atributos vivían en una clase por operación.
"""

from dataclasses import dataclass
from typing import Callable, List, Tuple


@dataclass(frozen=True)
class OperacionRegistrada:
    etiqueta: str
    entradas: List[Tuple[str, str]]
    funcion: Callable  # método ya ligado a la instancia de su categoría (Aritmetica, Discreta...)

    def __call__(self, *args):
        # Mismo rol que el __call__ que antes vivía en Operacion: permite
        # ejecutar `operacion_registrada(*args)` sin que quien llama sepa
        # si por dentro es sumar(), factorial() o seno().
        return self.funcion(*args)