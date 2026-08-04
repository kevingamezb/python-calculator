# Punto de Entrada Principal - Equipo Pochoclo + Alvaro
"""
Punto de entrada del programa: aquí vive el bucle principal.

Cómo funciona el flujo (en palabras simples):
  1. El usuario corre:  python main.py
  2. Este archivo crea la Calculadora y arma el menú a partir de su
     registro (interfaces/consola.construir_menu).
  3. El bucle while muestra el menú, pide una opción y la ejecuta,
     una y otra vez, hasta que el usuario elige "0. Salir".
  4. interfaces/consola.py aporta las piezas sueltas (mostrar_menu,
     ejecutar_operacion, etc.); este archivo es quien las conecta y
     decide cuándo parar.
  5. La Calculadora (nucleo/calculadora.py) busca la operación en su
     registro y la ejecuta con los datos que pidió la consola.
  6. Las operaciones concretas viven en operaciones/*.py.

Si en el futuro se agrega otra interfaz (por ejemplo gráfica), este
archivo podría preguntar primero cuál usar, en vez de ir directo a
la de consola.
"""

from nucleo.calculadora import Calculadora
from interfaces.consola import construir_menu, mostrar_menu, ejecutar_operacion


def main():
    calculadora = Calculadora()
    menu = construir_menu(calculadora)

    while True:
        try:
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
        except EOFError:
            print("Ha ocurrido un error. Intente de nuevo.\n")
        except KeyboardInterrupt:
            print("¡Hasta Luego!")
            break

if __name__ == '__main__':
    # Solo corre cuando ejecutamos este archivo directamente
    # (python main.py), no cuando se importa desde otro lado.
    main()