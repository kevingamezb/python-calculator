# Interfaz de Línea de Comandos - Andrés León & Shalon León
"""
Interfaz de consola mínima para probar la Calculadora.

Por ahora solo hay operaciones trigonométricas registradas en
`Calculadora`, así que este menú se limita a esas. Conforme el
resto del equipo termine sus módulos (aritméticas, discretas,
exponenciales, impuestos) y los agreguen al registro de
`calculadora.py`, este menú se puede ir ampliando.
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


def mostrar_menu(menu):
    print("\n=== Calculadora ===")
    for clave, (_, etiqueta) in menu.items():
        print(f"  {clave}. {etiqueta}")
    print("  0. Salir")


def ejecutar_operacion(calculadora, nombre_operacion):
    """Pide los datos necesarios y ejecuta la operación elegida."""
    # Las operaciones trigonométricas necesitan ángulo + unidad.
    # Las operaciones aritméticas e IVA necesitan dos números.

    global resultado
    try:
        if nombre_operacion in ('sen', 'cos', 'tan'):
            angulo = _pedir_float("Ángulo: ")
            unidad = _pedir_unidad()

            resultado = calculadora.calcular(nombre_operacion, angulo, unidad)

        elif nombre_operacion in ('Suma', 'Resta', 'Multiplicacion', 'Division', 'IVA'):
            numero_a = _pedir_float("Primer número: ")
            numero_b = _pedir_float("Segundo número: ")

            resultado = calculadora.calcular(nombre_operacion, numero_a, numero_b)

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