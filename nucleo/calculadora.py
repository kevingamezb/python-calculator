# Lógica Principal de la Calculadora - Alvaro Orjuela & Kevin Gámez
"""
Punto de entrada principal que conecta todas las subclases de `Operacion`
a través de un registro, exponiendo una única función `calcular` a la
capa de interfaces.
"""

from excepciones.error_calculadora import ErrorNumeroArgumentos, ErrorOperacionDesconocida
from operaciones.trigonometricas import Seno, Coseno, Tangente
from operaciones.aritmeticas import Suma, Resta, Multiplicacion, Division
from operaciones.discretas import Factorial, Fibonacci, MCM, MCD
from operaciones.exponenciales import Potencia, Raiz
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

        # `*args` (asterisco antes del nombre) significa "los argumentos
        # que sobren, guárdalos en una tupla llamada args". Así, calcular()
        # acepta cualquier cantidad de datos: dos números (Suma), ángulo +
        # unidad (Seno), un número (Factorial), etc.
        #
        # `clase_operacion(*args)` DESEMPAQUETA la tupla y le pasa los
        # valores uno por uno al constructor. Ejemplo: si args = (5, 3),
        # equivale a llamar Suma(5, 3).

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

        # operacion() ejecuta __call__ (definido en Operacion), que a su
        # vez llama a ejecutar(): el método que cada operación implementa.
        return operacion()

    def obtener_clase(self, nombre_operacion):
        """Devuelve la clase (no la instancia) registrada para ese nombre.

        Lo usa la interfaz de consola para leer el atributo `entradas`
        de la operación y pedir los datos correctos automáticamente,
        sin mantener listas de nombres a mano.
        """
        return self._operaciones[nombre_operacion]

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
        # List comprehension: construye una lista nueva recorriendo algo,
        # todo en una sola expresión. Se lee de derecha a izquierda:
        #
        #   for nombre, clase_operacion in self._operaciones.items()
        #       -> self._operaciones es un dict {'sen': Seno, 'cos': Coseno, ...}.
        #          .items() da pares (clave, valor): ('sen', Seno), ('cos', Coseno)...
        #          El for los va desempacando uno por uno: en cada vuelta,
        #          nombre = 'sen' y clase_operacion = Seno (la CLASE, no una
        #          instancia; nunca se hace Seno(...) aquí).
        #
        #   clase_operacion.etiqueta
        #       -> Seno.etiqueta vale 'Seno' porque quedó definido como
        #          atributo de clase en operaciones/trigonometricas.py.
        #          Al ser atributo de CLASE (no de instancia), se puede leer
        #          sin crear el objeto: no hace falta un ángulo para saber
        #          que Seno "se llama" Seno.
        #
        #   (nombre, clase_operacion.etiqueta)
        #       -> arma una tupla con esos dos valores: ('sen', 'Seno').
        #
        #   [ ... ]
        #       -> los corchetes de afuera dicen "guarda cada tupla que
        #          produce el for en una lista nueva". Sin ellos, esto no
        #          sería una list comprehension, solo una expresión suelta.
        #
        # ¿Por qué así y no con un for normal? Es exactamente el mismo
        # resultado que:
        #
        #   resultado = []
        #   for nombre, clase_operacion in self._operaciones.items():
        #       resultado.append((nombre, clase_operacion.etiqueta))
        #   return resultado
        #
        # pero en una sola expresión. Se usa aquí porque el caso es simple
        # (una vuelta, una transformación, sin condicionales) y evita crear
        # una variable intermedia (`resultado`) que solo se usa para
        # acumular y luego se retorna: menos líneas, misma lógica.
        return [
            (nombre, clase_operacion.etiqueta)
            for nombre, clase_operacion in self._operaciones.items()
        ]