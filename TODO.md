# TODO - Mejoras de la interfaz de consola

Mejoras pendientes para `interfaces/consola.py`. Cuando queden hechas,
marcarlas con `[x]`.

## Prioridad alta

- [ ] **Limpiar la terminal** antes de mostrar cada menú.
      En Windows se usa `cls`; en Linux/macOS, `clear`. Conviene una
      función `_limpiar_pantalla()` que elija el comando según el sistema:
      `os.system('cls' if os.name == 'nt' else 'clear')`.

- [ ] **Pausar cuando hay un error**: después de mostrar un error,
      esperar un Enter (`input("Presiona Enter para continuar...")`),
      para que el usuario alcance a leerlo antes de que se limpie la
      pantalla y se redibuje el menú.

- [ ] **Pausar también tras el resultado**, por la misma razón que el
      error: si la pantalla se limpia al volver al menú, el resultado
      desaparecería antes de que el usuario lo lea.

- [x] **Atrapar Ctrl+C (KeyboardInterrupt) y EOFError** en `main()`,
      para salir limpiamente ("¡Hasta luego!") sin imprimir un traceback.

## Prioridad media

- [ ] **Mostrar el último resultado en el menú** (ej. una línea
      "Resultado anterior: 16.0"), para que el usuario recuerde que
      puede reutilizarlo con Enter (modo acumulativo).

- [ ] **Formatear el resultado**: evitar la basura flotante
      (ej. `2.0000000000000004`) y decidir cuántos decimales mostrar.

## Futuro (mayor alcance)

- [ ] **Persistir el historial** de operaciones y resultados en un
      archivo, para que se conserve entre ejecuciones del programa.
- [ ] **Opción de menú para ver el historial** de operaciones.
