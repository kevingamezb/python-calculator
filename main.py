# Punto de Entrada Principal - Equipo Pochoclo + Alvaro
"""
Punto de entrada del programa.

Por ahora solo lanza la interfaz de consola. Cuando `grafica.py`
esté terminada, aquí se podría agregar un menú previo para elegir
entre consola o interfaz gráfica.
"""

from interfaces.consola import main as ejecutar_consola

if __name__ == '__main__':
    ejecutar_consola()
