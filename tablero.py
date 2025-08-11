
class PosOcupadaException(Exception):
    pass

class MovimientoInvalidoException(Exception):
    pass

class Tablero:
    def __init__(self):
        
        self.contenedor = [["" for _ in range(3)] for _ in range(3)]

    def _validar_rango(self, fila, col):
        if not (0 <= fila < 3 and 0 <= col < 3):
            raise IndexError("Coordenadas fuera del tablero (deben ser 0..2).")

    def mostrar(self):
        
        for i, fila in enumerate(self.contenedor):
            print(" | ".join(c if c != "" else " " for c in fila))
            if i < 2:
                print("--+---+--")

    def poner_ficha(self, fila, col, ficha):
        self._validar_rango(fila, col)
        if self.contenedor[fila][col] != "":
            raise PosOcupadaException("La casilla ya está ocupada.")
        self.contenedor[fila][col] = ficha

    def mover_ficha(self, fila_origen, col_origen, fila_destino, col_destino, ficha):
        self._validar_rango(fila_origen, col_origen)
        self._validar_rango(fila_destino, col_destino)

        if self.contenedor[fila_origen][col_origen] != ficha:
            raise MovimientoInvalidoException("No podés mover una ficha que no es tuya.")
        if self.contenedor[fila_destino][col_destino] != "":
            raise PosOcupadaException("La casilla de destino está ocupada.")

        self.contenedor[fila_origen][col_origen] = ""
        self.contenedor[fila_destino][col_destino] = ficha

    def hay_ganador(self, ficha):
        
        for i in range(3):
            if all(self.contenedor[i][j] == ficha for j in range(3)):
                return True
            if all(self.contenedor[j][i] == ficha for j in range(3)):
                return True
        
        if all(self.contenedor[i][i] == ficha for i in range(3)):
            return True
        if all(self.contenedor[i][2 - i] == ficha for i in range(3)):
            return True
        return False

    def contar_fichas(self, ficha):
        return sum(celda == ficha for fila in self.contenedor for celda in fila)
