# Punto de Entrada Principal - Equipo Pochoclo + Alvaro
"""
Punto de entrada del programa.

Por ahora solo lanza la interfaz de consola. Cuando `grafica.py`
esté terminada, aquí se podría agregar un menú previo para elegir
entre consola o interfaz gráfica.
"""

# Cómo funciona el flujo (en palabras simples):
#   1. El usuario corre:  python main.py
#   2. main() de interfaces/consola.py muestra el menú y pide una opción.
#   3. La Calculadora (nucleo/calculadora.py) busca la operación en su
#      registro y la ejecuta con los datos que pidió la consola.
#   4. Las operaciones concretas viven en operaciones/*.py.
#
# Importamos la función con un alias para que el nombre diga qué está
# pasando y no se confunda con este mismo archivo (main.py).
from interfaces.consola import main as ejecutar_consola

if __name__ == '__main__':
    # Solo corre cuando ejecutamos este archivo directamente
    # (python main.py), no cuando se importa desde otro lado.
    ejecutar_consola()
