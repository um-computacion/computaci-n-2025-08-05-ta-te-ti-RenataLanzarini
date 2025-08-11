from tateti import Tateti

def pedir_coord(msg):
    val = input(msg).strip()
    if val.lower() == "q":
        raise SystemExit
    n = int(val)
    if n < 0 or n > 2:
        raise IndexError("Las coordenadas deben estar entre 0 y 2.")
    return n

def main():
    print("🎮 Bienvenidos al Tateti dinámico (q para salir)\n")
    print("📜 Instrucciones rápidas:")
    print("- X (humano) vs O (CPU). X siempre empieza.")
    print("- Cada jugador tiene hasta 3 fichas. Luego deben mover.")
    print("- Gana quien alinee sus 3 fichas (fila/columna/diagonal).")
    print("- Ingrese coordenadas 0..2. Ej: fila 0, columna 1.\n")

    while True:
        juego = Tateti()

        try:
            while not juego.juego_terminado():
                juego.mostrar_tablero()
                print(f"\nTurno de: {juego.jugador_actual}  |  Fase: {juego.fase_actual()}")

                if juego.jugador_actual == "X":
                    if juego.fase_actual() == "colocacion":
                        try:
                            fila = pedir_coord("Fila destino (0-2): ")
                            col = pedir_coord("Columna destino (0-2): ")
                            juego.jugar(fila_destino=fila, col_destino=col)
                        except (ValueError, IndexError) as e:
                            print(f"⚠️ {e} (o 'q' para salir).")
                            continue
                    else:
                        try:
                            print("Mover ficha:")
                            fo = pedir_coord("Fila origen (0-2): ")
                            co = pedir_coord("Columna origen (0-2): ")
                            fd = pedir_coord("Fila destino (0-2): ")
                            cd = pedir_coord("Columna destino (0-2): ")
                            juego.jugar(fila_destino=fd, col_destino=cd, fila_origen=fo, col_origen=co)
                        except (ValueError, IndexError) as e:
                            print(f"⚠️ {e} (o 'q' para salir).")
                            continue
                else:
                    print("🤖 Jugada de O (CPU)...")
                    juego.jugar_cpu()

            juego.mostrar_tablero()
            print(f"\n🎉 ¡Ganó {juego.ganador}! 🎉")

        except SystemExit:
            print("\nSaliendo del juego. ¡Hasta la próxima!")
            break
        except KeyboardInterrupt:
            print("\n\nInterrumpido por el usuario. 👋")
            break

        opcion = input("\n¿Querés volver a jugar? (s/n): ").strip().lower()
        if opcion != "s":
            print("¡Gracias por jugar! 👋")
            break

if __name__ == "__main__":
    main()
