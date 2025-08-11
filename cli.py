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
    print("🎮 Bienvenidos al Tateti dinámico (q para salir)")
    juego = Tateti()

    try:
        while not juego.juego_terminado():
            juego.mostrar_tablero()
            print(f"\nTurno de: {juego.jugador_actual}")

            if juego.fichas_colocadas[juego.jugador_actual] < 3:
                try:
                    fila = pedir_coord("Fila destino (0-2): ")
                    col = pedir_coord("Columna destino (0-2): ")
                    juego.jugar(fila_destino=fila, col_destino=col)
                except ValueError:
                    print("⚠️ Debe ingresar números (o 'q' para salir).")
                except IndexError as e:
                    print(f"⚠️ {e}")
            else:
                try:
                    print("Mover ficha:")
                    fo = pedir_coord("Fila origen (0-2): ")
                    co = pedir_coord("Columna origen (0-2): ")
                    fd = pedir_coord("Fila destino (0-2): ")
                    cd = pedir_coord("Columna destino (0-2): ")
                    juego.jugar(fila_destino=fd, col_destino=cd, fila_origen=fo, col_origen=co)
                except ValueError:
                    print("⚠️ Debe ingresar números (o 'q' para salir).")
                except IndexError as e:
                    print(f"⚠️ {e}")

        juego.mostrar_tablero()
        print(f"\n🎉 ¡Ganó {juego.ganador}! 🎉")

    except SystemExit:
        print("\nSaliendo del juego. ¡Hasta la próxima!")
    except KeyboardInterrupt:
        print("\n\nInterrumpido por el usuario. 👋")

if __name__ == "__main__":
    main()

