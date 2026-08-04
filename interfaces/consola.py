# Interfaz de Línea de Comandos - Andrés León & Shalon León
"""
Interfaz de consola para probar la Calculadora.

El menú se construye a partir del registro real de `Calculadora`
(ver `operaciones_disponibles`), y cada operación declara las
entradas que necesita en su atributo `entradas` (ver
`nucleo/operacion.py`). Así, al registrar una operación nueva solo
hay que declararle sus entradas: este menú se las pide automáticamente.
"""

from nucleo.calculadora import Calculadora
from excepciones.error_calculadora import ErrorCalculadora


def _construir_menu(calculadora):
    """Genera el menú (clave de menú -> (nombre_operacion, etiqueta)) a
    partir del registro real de la Calculadora, en vez de mantener una
    lista aparte a mano. Así, cuando se agreguen operaciones al registro
    en nucleo/calculadora.py, el menú las incluye automáticamente sin
    tocar este archivo.
    """
    # Dict comprehension: igual que una list comprehension, pero hace
    # {clave: valor}. Recorre cada opción del registro, le asigna un
    # número de menú y guarda la tupla (nombre_operacion, etiqueta).
    # Ejemplo de una vuelta:
    #   indice = 1, nombre = 'sen', etiqueta = 'Seno'
    #   -> '1': ('sen', 'Seno')
    #
    # enumerate() va "numerando" una lista: devuelve (0, primero),
    # (1, segundo)... Con start=1 empezamos en 1 y no en 0, porque el
    # 0 lo reservamos para "Salir". str(indice) convierte el número a
    # texto, que es lo que se lee desde input().
    return {
        str(indice): (nombre, etiqueta)
        for indice, (nombre, etiqueta) in enumerate(
            calculadora.operaciones_disponibles(), start=1
        )
    }


def _pedir_float(mensaje):
    """Pide un número por consola, repitiendo hasta que sea válido."""
    while True:
        entrada = input(mensaje).strip()
        try:
            return float(entrada)
        except ValueError:
            print(f"  '{entrada}' no es un número válido. Intenta de nuevo.\n")


def _pedir_unidad():
    """Pide 'radianes' o 'grados', repitiendo hasta que sea válida.
    Deja 'radianes' por defecto si el usuario no escribe nada.
    """
    while True:
        entrada = input("Unidad del ángulo (radianes/grados) [radianes]: ").strip().lower()
        if not entrada:
            return 'radianes'
        if entrada in ('radianes', 'grados'):
            return entrada
        print(f"  '{entrada}' no es una unidad válida. Usa 'radianes' o 'grados'.")


def _pedir_entradas(clase_operacion):
    """Pide las entradas que la operación declara en su atributo
    `entradas`: lista de tuplas (etiqueta, tipo), donde tipo es
    'numero' o 'unidad'. Devuelve los valores en el mismo orden.
    """
    valores = []
    for etiqueta, tipo in clase_operacion.entradas:
        if tipo == 'numero':
            valores.append(_pedir_float(f"{etiqueta}: "))
        elif tipo == 'unidad':
            valores.append(_pedir_unidad())
    return valores


def mostrar_menu(menu):
    print("\n=== Calculadora ===")
    for clave, (_, etiqueta) in menu.items():
        print(f"  {clave}. {etiqueta}")
    print("  0. Salir")


def ejecutar_operacion(calculadora, nombre_operacion):
    """Pide las entradas que la operación declara y la ejecuta."""
    try:
        entradas = _pedir_entradas(calculadora.obtener_clase(nombre_operacion))
        # `*entradas` DESEMPAQUETA la lista: si entradas = [5, 3], es
        # como escribir calcular('Suma', 5, 3). Así le pasamos a la
        # Calculadora tantos datos como la operación pida, sin importar
        # cuántos sean.
        resultado = calculadora.calcular(nombre_operacion, *entradas)
        print(f"\nResultado: {resultado}")

    except ErrorCalculadora as e:
        # Capturamos la clase base: cualquier error propio de la
        # calculadora (unidad inválida, división por cero, etc.)
        # cae aquí sin necesidad de un except por cada tipo.
        print(f"\nError: {e.mensaje}")


def main():
    calculadora = Calculadora()
    menu = _construir_menu(calculadora)

    while True:
        mostrar_menu(menu)
        opcion = input("\nElige una opción: ").strip()

        if opcion == '0':
            print("¡Hasta luego!")
            break

        if opcion not in menu:
            print("\nOpción no válida. Intenta de nuevo.")
            continue

        nombre_operacion, _ = menu[opcion]
        ejecutar_operacion(calculadora, nombre_operacion)


if __name__ == '__main__':
    main()