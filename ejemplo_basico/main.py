# Ejemplo Sencillo (No tan modular como el código fuente [https://github.com/kevingamezb/python-calculator])
# De Calculadora en python.
# Equipo Pochoclo + Alvarito
# - Kevin Sebastián Gámez Benítez (1804920)
# - Andres Felipe Leon            (1804913)
# - Shalon Valentiana León        (1804926)
# - Alvaro


# Imports

import os
from abc import ABC, abstractmethod
from math import sin, cos, tan, isclose, radians


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

class TangenteNoDefinida(ErrorCalculadora):
    mensaje_por_defecto = "La tangente no está definida para esta entrada."

class EntradaNoValida(ErrorCalculadora):
    mensaje_por_defecto = "Entrada no válida"

class DivisionPorCero(ErrorCalculadora):
    mensaje_por_defecto = "No se permite la división por cero."

class FactorialNegativo(ErrorCalculadora):
    mensaje_por_defecto = "El factorial no está definido para números negativos."

class FactorialNoEntero(ErrorCalculadora):
    mensaje_por_defecto = "El factorial solo está definido para números enteros."

class FibonacciNegativo(ErrorCalculadora):
    mensaje_por_defecto = "El fibonacci no está definido para números negativos."

class NumeroImaginario(ErrorCalculadora):
    mensaje_por_defecto = "La operación resultó en un número imaginario."

class PotenciaIndefinida(ErrorCalculadora):
    mensaje_por_defecto = "La potencia está indefinida para esta operación."

class OperacionDesconocida(ErrorCalculadora):
    mensaje_por_defecto = "Operación desconocida."

class NumeroArgumentos(ErrorCalculadora):
    mensaje_por_defecto = "Número incorrecto de argumentos."


# Clases Principales (Operación (con funciones [operaciones]) y Calculadora [Kevin Gámez & Andrés León])
# - Trigonométricas (Kevin Gámez)
# - Aritméticas (Shalon León)
# - Impuestos (Shalon León)
# - Discretas (Andrés León & Alvaro Orjuela [Factorial])
# - Exponenciales (Alvaro Orjuela)


# Clase base de todas las operaciones. Cada operación concreta declara
# en `entradas` los datos que necesita (lista de tuplas (etiqueta, tipo)),
# y la consola los pide automáticamente leyendo ese atributo.

class Operacion(ABC):

    entradas = []

    @abstractmethod
    def ejecutar(self):
        pass

    def __call__(self):
        return self.ejecutar()


# Artiméticas (Shalon León)

class Suma(Operacion):
    etiqueta = 'Suma'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        return self._numero_a + self._numero_b

class Resta(Operacion):
    etiqueta = 'Resta'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        return self._numero_a - self._numero_b

class Multiplicacion(Operacion):
    etiqueta = 'Multiplicación'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        return self._numero_a * self._numero_b

class Division(Operacion):
    etiqueta = 'División'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        # La división entre 0 no existe; lanzamos nuestro propio error
        # para que la consola lo muestre bonito.
        if self._numero_b == 0:
            raise DivisionPorCero()
        return self._numero_a / self._numero_b


# Exponenciales (Alvaro Orjuela)

class Potencia(Operacion):
    etiqueta = 'Potencia'
    entradas = [('Base', 'numero'), ('Exponente', 'numero')]

    def __init__(self, base, exponente):
        self._base = base
        self._exponente = exponente

    def ejecutar(self):
        # 0^0 es un caso indefinido en matemáticas.
        if self._base == 0 and self._exponente == 0:
            raise PotenciaIndefinida()
        # Un negativo elevado a un exponente NO entero da un imaginario.
        if self._base < 0 and not float(self._exponente).is_integer():
            raise NumeroImaginario()
        return self._base ** self._exponente

class Raiz(Operacion):
    etiqueta = 'Raíz'
    entradas = [('Radicando', 'numero'), ('Índice', 'numero')]

    def __init__(self, radicando, indice):
        self._radicando = radicando
        self._indice = indice

    def ejecutar(self):
        # El índice es el numerito de la raíz: en la cuadrada es 2.
        if self._indice == 0:
            raise EntradaNoValida("El índice de la raíz no puede ser cero.")

        if self._radicando < 0:
            # Índice IMPAR: la raíz de un negativo existe y da negativo.
            if float(self._indice).is_integer() and self._indice % 2 != 0:
                return -((-self._radicando) ** (1 / self._indice))
            # Índice PAR (o no entero): el resultado sería imaginario.
            raise NumeroImaginario()

        # La raíz n-ésima es lo mismo que elevar a 1/n.
        return self._radicando ** (1 / self._indice)


# Trigonométricas (Kevin Gámez)

_UNIDADES_VALIDAS = ('radianes', 'grados')

class OperacionAngular(Operacion, ABC):
    # Base común: valida la unidad y convierte a radianes.
    entradas = [('Ángulo', 'numero'), ('Unidad', 'unidad')]

    def __init__(self, angulo, unidad='radianes'):
        unidad = unidad.lower() if isinstance(unidad, str) else ''
        if unidad not in _UNIDADES_VALIDAS:
            raise UnidadInvalida()
        self._angulo = angulo
        self._unidad = unidad

    def _angulo_en_radianes(self):
        angulo = self._angulo
        if self._unidad == 'grados':
            angulo = radians(angulo)
        return angulo

class Seno(OperacionAngular):
    etiqueta = 'Seno'

    def ejecutar(self):
        return sin(self._angulo_en_radianes())

class Coseno(OperacionAngular):
    etiqueta = 'Coseno'

    def ejecutar(self):
        return cos(self._angulo_en_radianes())

class Tangente(OperacionAngular):
    etiqueta = 'Tangente'

    def ejecutar(self):
        angulo = self._angulo_en_radianes()
        # isclose() en vez de == 0: por errores de precisión de punto
        # flotante, cos(x) casi nunca da exactamente 0.
        if isclose(cos(angulo), 0, abs_tol=1e-9):
            raise TangenteNoDefinida()
        return tan(angulo)


# Discretas (Andrés León & Alvaro Orjuela [Factorial])

def _es_entero_positivo(numero):
    """True si el número es un entero mayor que cero (12 y 12.0 valen)."""
    return float(numero).is_integer() and numero > 0

class Factorial(Operacion):
    etiqueta = 'Factorial'
    entradas = [('Número', 'numero')]

    def __init__(self, numero_a):
        self._numero_a = numero_a

    def ejecutar(self):
        if self._numero_a < 0:
            raise FactorialNegativo()
        if not float(self._numero_a).is_integer():
            raise FactorialNoEntero()
        if self._numero_a == 0 or self._numero_a == 1:
            return 1
        # RECURSIÓN: n! = n * (n-1)!  |  El () al final llama a ejecutar().
        return self._numero_a * Factorial(self._numero_a - 1)()

class Fibonacci(Operacion):
    etiqueta = 'Fibonacci'
    entradas = [('Término', 'numero')]

    def __init__(self, numero):
        self._numero = numero

    def ejecutar(self):
        n = self._numero

        if n < 0:
            raise FibonacciNegativo()
        if not float(n).is_integer():
            raise EntradaNoValida("El fibonacci solo está definido para enteros.")

        # La consola manda floats (10.0); range() exige int.
        n = int(n)

        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b

class MCM(Operacion):
    etiqueta = 'Mínimo Común Múltiplo'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        for numero in (self._numero_a, self._numero_b):
            if not _es_entero_positivo(numero):
                raise EntradaNoValida("El MCM solo está definido para enteros positivos.")

        # Fórmula: MCM(a, b) = a * b / MCD(a, b)
        #   Ejemplo: MCM(12, 18) = 12 * 18 / MCD(12, 18) = 216 / 6 = 36
        # Reutilizamos la clase MCD (definida más abajo), que ya sabe
        # cómo calcular el máximo común divisor.
        mcd = MCD(self._numero_a, self._numero_b).ejecutar()
        return self._numero_a * self._numero_b // mcd

class MCD(Operacion):
    etiqueta = 'Máximo Común Divisor'
    entradas = [('Primer número', 'numero'), ('Segundo número', 'numero')]

    def __init__(self, numero_a, numero_b):
        self._numero_a = numero_a
        self._numero_b = numero_b

    def ejecutar(self):
        for numero in (self._numero_a, self._numero_b):
            if not _es_entero_positivo(numero):
                raise EntradaNoValida("El MCD solo está definido para enteros positivos.")

        # Algoritmo de Euclides: MCD(a, b) = MCD(b, a % b)
        #   Ejemplo: MCD(12, 18) = MCD(18, 12) = MCD(12, 6) = MCD(6, 0) = 6
        a, b = self._numero_a, self._numero_b
        while b != 0:
            a, b = b, a % b
        return a


# Impuestos (Shalon León)

class IVA(Operacion):
    etiqueta = 'IVA'
    entradas = [('Monto', 'numero'), ('Porcentaje', 'numero')]

    def __init__(self, monto, porcentaje):
        self._monto = monto
        self._porcentaje = porcentaje

    def ejecutar(self):
        # Regla de tres: el "porcentaje de algo" = monto * porcentaje / 100.
        # Ejemplo: 100 * 19 / 100 = 19.
        return self._monto * self._porcentaje / 100


# Calculadora (Kevin Gámez & Andrés León)

class Calculadora:
    """
    Enruta las solicitudes de operación hacia la clase correcta, usando
    un registro construido al momento de la creación. Guarda el último
    resultado en memoria para el modo acumulativo.
    """

    def __init__(self):
        # Registro: mapea el nombre de la operación (lo que el usuario
        # elige en el menú) a la CLASE correspondiente. Se instancia cada
        # vez en calcular(), porque cada operación necesita datos distintos.
        self._operaciones = {
            'Suma'          :  Suma,
            'Resta'         :  Resta,
            'Multiplicacion':  Multiplicacion,
            'Division'      :  Division,
            'Potencia'      :  Potencia,
            'Raiz'          :  Raiz,
            'sen'           :  Seno,
            'cos'           :  Coseno,
            'tan'           :  Tangente,
            'IVA'           :  IVA,
            'Factorial'     :  Factorial,
            'Fibonacci'     :  Fibonacci,
            'MCM'           :  MCM,
            'MCD'           :  MCD,
        }

        # Memoria de la calculadora: el último resultado calculado, para
        # que la interfaz lo ofrezca como entrada por defecto.
        self._ultimo_resultado = None

    def calcular(self, nombre_operacion, *args):
        """
        Ejecuta la operación identificada por `nombre_operacion` con los
        argumentos dados, guarda el resultado en memoria y lo devuelve.
        """
        if nombre_operacion not in self._operaciones:
            raise OperacionDesconocida(f"Operación desconocida: {nombre_operacion}")

        clase_operacion = self._operaciones[nombre_operacion]

        # `*args` desempaqueta los datos y se los pasa al constructor:
        # si args = (5, 3), equivale a llamar Suma(5, 3). Capturamos
        # TypeError porque es lo que Python lanza si faltan o sobran
        # argumentos, y lo traducimos a nuestra jerarquía de errores.
        try:
            operacion = clase_operacion(*args)
        except TypeError as e:
            raise NumeroArgumentos(
                f"Número incorrecto de argumentos para '{nombre_operacion}': {e}"
            )

        # operacion() llama a __call__ (definido en Operacion), que a su
        # vez llama a ejecutar().
        resultado = operacion()

        # Redondeamos ANTES de guardar en memoria, no solo al imprimir:
        # los floats arrastran "basura" de precisión binaria (0.1 + 0.2
        # da 0.30000000000000004). Si guardáramos el valor crudo, esa
        # basura se propagaría a la siguiente operación.
        if isinstance(resultado, float):
            resultado = round(resultado, 5)

        self._ultimo_resultado = resultado
        return resultado

    def ultimo_resultado(self):
        return self._ultimo_resultado

    def obtener_clase(self, nombre_operacion):
        return self._operaciones[nombre_operacion]

    def operaciones_disponibles(self):
        # List comprehension: construye la lista (nombre, etiqueta) para
        # que la consola arme el menú automáticamente desde el registro.
        return [
            (nombre, clase_operacion.etiqueta)
            for nombre, clase_operacion in self._operaciones.items()
        ]


# Interfaz de consola (ver interfaces/consola.py del código fuente)

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pausar_mensaje(mensaje):
    if mensaje == '':
        input("Presione Enter para continuar...")
    else:
        print(mensaje + '\n')
        input("Presione Enter para continuar...")

def _pedir_float(mensaje, por_defecto=None):
    """
    Pide un número por consola, repitiendo hasta que sea válido. Si
    `por_defecto` viene dado (p. ej. el último resultado) y el usuario
    solo presiona Enter, se usa ese valor (modo acumulativo).
    """
    while True:
        if por_defecto is not None:
            entrada = input(f"{mensaje} [{por_defecto}]: ").strip()
            if not entrada:
                return por_defecto
        else:
            entrada = input(mensaje).strip()

        try:
            return float(entrada)
        except ValueError:
            print(f"'{entrada}' no es un número válido. Intenta de nuevo.\n")
            pausar_mensaje('')

def _pedir_unidad():
    """Pide 'radianes' o 'grados', con 'radianes' por defecto."""
    while True:
        entrada = input("Unidad del ángulo (radianes/grados) [radianes]: ").strip().lower()
        if not entrada:
            return 'radianes'
        if entrada in ('radianes', 'grados'):
            return entrada
        print(f" '{entrada}' no es una unidad válida. Usa 'radianes' o 'grados'.")
        pausar_mensaje('')

def _pedir_entradas(clase_operacion, por_defecto=None):
    """
    Pide las entradas que la operación declara en `entradas`. El último
    resultado se ofrece solo en el PRIMER campo numérico, así se puede
    encadenar una operación con la anterior presionando Enter.
    """
    primer_numero = True
    valores = []
    for etiqueta, tipo in clase_operacion.entradas:
        if tipo == 'numero':
            if primer_numero:
                valores.append(_pedir_float(f"{etiqueta}: ", por_defecto))
                primer_numero = False
            else:
                valores.append(_pedir_float(f"{etiqueta}: "))
        elif tipo == 'unidad':
            valores.append(_pedir_unidad())
    return valores

def construir_menu(calculadora):
    """
    Genera el menú (clave de menú -> (nombre_operacion, etiqueta)) a
    partir del registro real de la Calculadora, en vez de mantener una
    lista aparte a mano.
    """
    return {
        str(indice): (nombre, etiqueta)
        for indice, (nombre, etiqueta) in enumerate(
            calculadora.operaciones_disponibles(), start=1
        )
    }

def mostrar_menu(menu):
    print("\n=== Calculadora ===")
    for clave, (_, etiqueta) in menu.items():
        print(f"  {clave}. {etiqueta}")
    print("  0. Salir")

def ejecutar_operacion(calculadora, nombre_operacion):
    """
    Pide las entradas que la operación declara y la ejecuta, pasando el
    último resultado como entrada por defecto (modo acumulativo).
    """
    try:
        entradas = _pedir_entradas(
            calculadora.obtener_clase(nombre_operacion),
            calculadora.ultimo_resultado(),
        )
        # `*entradas` desempaqueta la lista: si entradas = [5, 3], es
        # como escribir calcular('Suma', 5, 3).
        resultado = calculadora.calcular(nombre_operacion, *entradas)
        print(f"\nResultado: {resultado}")
        pausar_mensaje('')

    except ErrorCalculadora as e:
        # Atrapamos la clase base: cualquier error propio de la
        # calculadora (unidad inválida, división por cero, etc.) cae
        # aquí sin necesidad de un except por cada tipo.
        print(f"\nError: {e.mensaje}")
        pausar_mensaje('')


# Bucle Principal (Kevin Gámez)

def main():
    calculadora = Calculadora()
    menu = construir_menu(calculadora)

    while True:
        try:
            limpiar_pantalla()
            mostrar_menu(menu)
            opcion = input("\nElige una opción: ").strip()

            if opcion == '0':
                print("¡Hasta luego!")
                break

            if opcion not in menu:
                pausar_mensaje("\nOpción no válida. Intenta de nuevo.")
                continue

            nombre_operacion, _ = menu[opcion]
            ejecutar_operacion(calculadora, nombre_operacion)
        except EOFError:
            pausar_mensaje("Ha ocurrido un error. Intente de nuevo.\n")
        except KeyboardInterrupt:
            print("¡Hasta Luego!")
            break

if __name__ == '__main__':
    main()
