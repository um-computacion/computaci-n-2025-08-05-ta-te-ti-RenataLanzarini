
from tablero import Tablero, PosOcupadaException, MovimientoInvalidoException

class Tateti:
    def __init__(self):
        self.tablero = Tablero()
        self.jugador_actual = "X"  
        self.fichas_colocadas = {"X": 0, "O": 0}
        self.ganador = None

    def jugar(self, fila_destino, col_destino, fila_origen=None, col_origen=None):
        if self.ganador:
            raise Exception("El juego ya terminó.")

        try:
            if self.fichas_colocadas[self.jugador_actual] < 3:
               
                self.tablero.poner_ficha(fila_destino, col_destino, self.jugador_actual)
                self.fichas_colocadas[self.jugador_actual] += 1
            else:
               
                if fila_origen is None or col_origen is None:
                    raise ValueError("Debe indicar origen para mover la ficha.")
                self.tablero.mover_ficha(fila_origen, col_origen, fila_destino, col_destino, self.jugador_actual)

           
            if self.tablero.hay_ganador(self.jugador_actual):
                self.ganador = self.jugador_actual

            
            self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

        except (PosOcupadaException, MovimientoInvalidoException, ValueError) as e:
            print(f"⚠️ Error: {e}")
            print("Intentá de nuevo. No perdés el turno.")

    def mostrar_tablero(self):
        self.tablero.mostrar()

    def juego_terminado(self):
        return self.ganador is not None
