# Lógica Principal de la Calculadora - Alvaro Orjuela & Kevin Gámez
"""
Punto de entrada principal que conecta las 4 clases de categoría
(Aritmetica, Discreta, Exponencial, Trigonometrica) a través de un
registro, exponiendo una única función `calcular` a la capa de
interfaces.
"""

from excepciones.error_calculadora import ErrorNumeroArgumentos, ErrorOperacionDesconocida
from nucleo.operacion import OperacionRegistrada
from operaciones.aritmeticas import Aritmetica
from operaciones.discretas import Discreta
from operaciones.exponenciales import Exponencial
from operaciones.trigonometricas import Trigonometrica

# Las 4 categorías de operación. Agregar una operación nueva a una
# categoría existente (ej. una nueva operación discreta) es tan simple
# como añadir un método a su clase y una entrada a su diccionario
# `OPERACIONES` — no hace falta tocar este archivo. Agregar una
# categoría nueva sí requiere añadir su clase aquí.
_CATEGORIAS = [Aritmetica, Discreta, Exponencial, Trigonometrica]


def _construir_registro():
    """
    Recorre las clases de _CATEGORIAS, instancia cada una una sola vez,
    y por cada entrada de su diccionario `OPERACIONES` arma un
    `OperacionRegistrada` (ver nucleo/operacion.py) que ata la
    etiqueta y las entradas al MÉTODO ya ligado a esa instancia.

    Devuelve el mismo tipo de estructura que antes (un dict
    nombre_operacion -> algo invocable con .etiqueta/.entradas), así
    que el resto de esta clase y toda la interfaz de consola no
    necesitan saber que por dentro cambió el diseño.
    """
    registro = {}
    for clase_categoria in _CATEGORIAS:
        instancia = clase_categoria()
        for nombre_operacion, (nombre_metodo, etiqueta, entradas) in clase_categoria.OPERACIONES.items():
            metodo = getattr(instancia, nombre_metodo)
            registro[nombre_operacion] = OperacionRegistrada(etiqueta, entradas, metodo)
    return registro


class Calculadora:
    """
    Enruta las solicitudes de operación hacia el método correcto de su
    categoría, usando un registro construido al momento de la creación.
    """

    def __init__(self):
        # Registro: mapea el nombre de la operación (lo que el usuario
        # elige en el menú) a un OperacionRegistrada (etiqueta,
        # entradas, y el método ya listo para llamarse).
        self._operaciones = _construir_registro()

        # Memoria de la calculadora: guarda el último resultado calculado
        # para que la interfaz pueda ofrecerlo como entrada por defecto
        # en la siguiente operación (modo acumulativo).
        self._ultimo_resultado = None

    def calcular(self, nombre_operacion, *args):
        """
        Ejecuta la operación identificada por `nombre_operacion` con los
        argumentos dados.

        Argumentos:
            nombre_operacion (str): clave registrada en self._operaciones.
            *args: argumentos que se pasan al método de la operación.

        Retorna:
            El resultado numérico de la operación.

        Lanza:
            ErrorOperacionDesconocida: si el nombre de la operación es desconocido.
            ErrorNumeroArgumentos: si el número de argumentos no coincide con lo
                que el método de la operación espera.

        Nota:
            Al terminar con éxito, guarda el resultado en `_ultimo_resultado`
            (la "memoria" de la calculadora), para que la interfaz pueda
            ofrecerlo como entrada por defecto en la siguiente operación.
        """
        if nombre_operacion not in self._operaciones:
            raise ErrorOperacionDesconocida(f"Operación desconocida: {nombre_operacion}")

        operacion_registrada = self._operaciones[nombre_operacion]

        # `*args` (asterisco antes del nombre) significa "los argumentos
        # que sobren, guárdalos en una tupla llamada args". Así, calcular()
        # acepta cualquier cantidad de datos: dos números (Suma), ángulo +
        # unidad (Seno), un número (Factorial), etc.
        #
        # `operacion_registrada(*args)` DESEMPAQUETA la tupla y llama al
        # método real (sumar, seno, factorial...) con esos valores.

        # Capturamos TypeError aquí porque es lo que Python lanza
        # automáticamente si faltan o sobran argumentos al llamar al
        # método — lo traducimos a nuestra propia jerarquía de
        # excepciones para mantener consistencia con el resto del sistema.
        try:
            resultado = operacion_registrada(*args)
        except TypeError as e:
            raise ErrorNumeroArgumentos(
                f"Número incorrecto de argumentos para '{nombre_operacion}': {e}"
            )

        # Redondeamos ANTES de guardar en memoria, no solo al imprimir.
        # Los floats en Python arrastran "basura" de precisión binaria
        # (ej. 0.1 + 0.2 da 0.30000000000000004, no 0.3 exacto). Si
        # guardáramos el valor crudo, esa basura se propagaría a la
        # siguiente operación en modo acumulativo (ultimo_resultado).
        if isinstance(resultado, float):
            resultado = round(resultado, 5)

        # Guardamos el resultado en la memoria. Si la operación lanzó un
        # error, esta línea nunca se alcanza y la memoria no cambia.
        self._ultimo_resultado = resultado
        return resultado

    def ultimo_resultado(self):
        """
        Devuelve el último resultado calculado (o None si aún no se
        ha calculado nada). La consola lo usa como entrada por defecto
        para encadenar operaciones.
        """
        return self._ultimo_resultado

    def obtener_operacion(self, nombre_operacion):
        """
        Devuelve el OperacionRegistrada asociado a ese nombre.

        Lo usa la interfaz de consola para leer el atributo `entradas`
        de la operación y pedir los datos correctos automáticamente,
        sin mantener listas de nombres a mano. Antes se llamaba
        `obtener_clase` porque devolvía una clase; ahora devuelve un
        OperacionRegistrada, pero expone los mismos atributos
        (.entradas, .etiqueta) que consola.py necesita.
        """
        return self._operaciones[nombre_operacion]

    def operaciones_disponibles(self):
        """
        Devuelve el registro de operaciones disponibles como una lista
        de tuplas (nombre_operacion, etiqueta), en el orden en que fueron
        registradas.
        """
        return [
            (nombre, operacion_registrada.etiqueta)
            for nombre, operacion_registrada in self._operaciones.items()
        ]