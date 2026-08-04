# Ejemplo Sencillo (No tan modular como el código fuente [https://github.com/kevingamezb/python-calculator])
# De Calculadora en python.
# Equipo Pochoclo + Alvarito
# - Kevin Sebastián Gámez Benítez (1804920)
# - Andres Felipe Leon (1804913)
# - Shalon Valentina León (1804926)
# - Alvaro Gay


# Imports

from math import sin, cos, tan, isclose, radians
from excepciones.error_calculadora import ErrorUnidadInvalida


# Excepciones Personalizadas (Kevin Gámez)

class ErrorCalculadora(Exception):
    mensaje_por_defecto = "Error en la calculadora."

    def __init__(self, mensaje=None):
        # Si quien lanzó el error no pasó mensaje, usamos el
        # mensaje_por_defecto de la clase concreta que se lanzó.
        self.mensaje = mensaje if mensaje is not None else self.mensaje_por_defecto
        super().__init__(self.mensaje)

class UnidadInvalida(ErrorCalculadora):
    mensaje_por_defecto = "Unidad de ángulo no válida. Usa 'radianes' o 'grados'"


# Clases Principales (Operación (con funciones [operaciones]) y Calculadora [Kevin Gámez & Andrés León])
# - Trigonométricas (Kevin Gámez)
# - Aritméticas (Shalon León)
# - Impuestos (Shalon León)
# - Discretas (Andrés León & Alvaro Orjuela [Factorial])
# - Exponenciales (Alvaro Orjuela)

class Operacion:

    # Artiméticas



    # Exponenciales



    # Trigonométricas

    @staticmethod
    def _angulo_en_radianes(angulo, unidad):
        angulos = ['radianes', 'grados']
        if unidad.lower() not in angulos:
            raise ErrorUnidadInvalida
        if unidad.lower() == 'grados':
            angulo = radians(angulo)
        return angulo

    @staticmethod
    def Seno():
        angulo = float(input("Ángulo: "))
        unidad = input("Unidad: ")

        return sin(Operacion._angulo_en_radianes(angulo, unidad))

    # Discretas
    
    def MCM(): 
            for numero in (num1, num2):
                if not _es_entero_positivo(numero):
                raise ErrorEntradaNoValida("El MCM solo está definido para enteros positivos.")

        # Fórmula: MCM(a, b) = a * b / MCD(a, b)
        #   Ejemplo: MCM(12, 18) = 12 * 18 / MCD(12, 18) = 216 / 6 = 36
        # Reutilizamos la clase MCD (definida más abajo), que ya sabe
        # cómo calcular el máximo común divisor.

        mcd = MCD(num1,num2).ejecutar()
        return num1 * num2 // mcd

    def MCD():
        for numero in (num1, num2):
            if not _es_entero_positivo(numero):
                raise ErrorEntradaNoValida("El MCD solo está definido para enteros positivos.")

        # Algoritmo de Euclides: MCD(a, b) = MCD(b, a % b)
        #   Ejemplo: MCD(12, 18) = MCD(18, 12) = MCD(12, 6) = MCD(6, 0) = 6
        
        a, b = num1, num2
        while b != 0:
            a, b = b, a % b
        return a



    # Impuestos




# Bucle Principal (Kevin Gámez)


