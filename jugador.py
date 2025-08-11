
class Jugador:
    def __init__(self, simbolo):
        if simbolo not in ("X", "O"):
            raise ValueError("El símbolo debe ser 'X' u 'O'.")
        self.simbolo = simbolo
