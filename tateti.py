from tablero import Tablero, PosOcupadaException, MovimientoInvalidoException
from jugador import Jugador

class Tateti:
    """
    Reglas clave:
    - Siempre empieza X.
    - Cada jugador coloca hasta tener 3 fichas. Luego SOLO puede mover una ficha propia a una casilla vacía.
    - Al producirse una jugada ganadora, el juego termina y NO se cambia el turno.
    - Si hay error (posición ocupada, mover ficha ajena, coordenadas inválidas), NO se pierde el turno.
    - Modo CPU: O juega automáticamente (estrategia simple).
    """

    def __init__(self):
        self.tablero = Tablero()
        self.jugador_x = Jugador("X")
        self.jugador_o = Jugador("O")
        self.jugador_actual = self.jugador_x.simbolo  
        self.fichas_colocadas = {"X": 0, "O": 0}
        self.ganador = None

    # ---------- Helpers de estado ----------
    def fase_actual(self):
        """'colocacion' si el jugador actual tiene < 3 fichas en el tablero; si no, 'movimiento'."""
        return "colocacion" if self.fichas_colocadas[self.jugador_actual] < 3 else "movimiento"

    def _cambiar_turno(self):
        self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def jugador_objeto_actual(self):
        return self.jugador_x if self.jugador_actual == "X" else self.jugador_o

    def jugar(self, fila_destino, col_destino, fila_origen=None, col_origen=None):
        """
        Ejecuta un turno:
        - En fase de 'colocacion': pone una ficha del jugador actual en (fila_destino, col_destino).
        - En fase de 'movimiento': mueve una ficha del jugador actual desde (fila_origen, col_origen) a (fila_destino, col_destino).
        Reglas de error: ante cualquier excepción validada, NO se cambia el turno.
        """
        if self.ganador:
            raise Exception("El juego ya terminó.")

        try:
            if self.fase_actual() == "colocacion":

                self.tablero.poner_ficha(fila_destino, col_destino, self.jugador_actual)
                self.fichas_colocadas[self.jugador_actual] += 1
            else:

                if fila_origen is None or col_origen is None:
                    raise ValueError("Debe indicar origen (fila_origen, col_origen) para mover la ficha.")
                self.tablero.mover_ficha(
                    fila_origen, col_origen, fila_destino, col_destino, self.jugador_actual
                )

            if self.tablero.hay_ganador(self.jugador_actual):
                self.ganador = self.jugador_actual
                return 

            self._cambiar_turno()

        except (PosOcupadaException, MovimientoInvalidoException, ValueError, IndexError) as e:
            print(f"⚠️ Error: {e}")
            print("Intentá de nuevo. No perdés el turno.")

    def _celdas_vacias(self):
        vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero.contenedor[i][j] == "":
                    vacias.append((i, j))
        return vacias

    def _celdas_de(self, ficha):
        propias = []
        for i in range(3):
            for j in range(3):
                if self.tablero.contenedor[i][j] == ficha:
                    propias.append((i, j))
        return propias

    def jugar_cpu(self):
        """
        Realiza una jugada automática para el jugador_actual (pensado para 'O').
        Estrategia:
          - Fase colocación: coloca en la primera casilla vacía.
          - Fase movimiento: si existe un movimiento ganador, lo hace; si no, mueve la primera ficha propia a la primera vacía.
        """
        if self.ganador:
            return

        ficha = self.jugador_actual

        if self.fase_actual() == "colocacion":
            vacias = self._celdas_vacias()
            if not vacias:
                return
            fi, cj = vacias[0]
            self.jugar(fi, cj)
            return

        propias = self._celdas_de(ficha)
        vacias = self._celdas_vacias()

        for oi, oj in propias:
            for di, dj in vacias:
                self.tablero.contenedor[oi][oj] = ""
                self.tablero.contenedor[di][dj] = ficha
                gana = self.tablero.hay_ganador(ficha)
                self.tablero.contenedor[di][dj] = ""
                self.tablero.contenedor[oi][oj] = ficha

                if gana:
                    self.jugar(di, dj, oi, oj)
                    return

        if propias and vacias:
            oi, oj = propias[0]
            di, dj = vacias[0]
            self.jugar(di, dj, oi, oj)

    def mostrar_tablero(self):
        self.tablero.mostrar()

    def juego_terminado(self):
        return self.ganador is not None

    def reset(self):
        """Reinicia el juego (útil para volver a jugar o para tests)."""
        self.__init__()
