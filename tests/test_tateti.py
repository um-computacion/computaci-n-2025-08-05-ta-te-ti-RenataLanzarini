import unittest
from tateti import Tateti
from tablero import PosOcupadaException, MovimientoInvalidoException

class TestTatetiBasico(unittest.TestCase):
    def test_empieza_x(self):
        juego = Tateti()
        self.assertEqual(juego.jugador_actual, "X")

    def test_cambio_turno_despues_de_jugar(self):
        juego = Tateti()
        juego.jugar(0, 0)
        self.assertEqual(juego.jugador_actual, "O")

    def test_posicion_ocupada_no_pierde_turno(self):
        juego = Tateti()
        juego.jugar(0, 0)  
        juego.jugar(0, 0)  
        self.assertEqual(juego.jugador_actual, "O")

    def test_ganar_fila(self):
        juego = Tateti()
        juego.jugar(0, 0)  
        juego.jugar(1, 0)  
        juego.jugar(0, 1)  
        juego.jugar(1, 1)  
        juego.jugar(0, 2)  
        self.assertTrue(juego.juego_terminado())
        self.assertEqual(juego.ganador, "X")

    def test_ganar_columna(self):
        juego = Tateti()
        juego.jugar(0, 0)  
        juego.jugar(0, 1)  
        juego.jugar(1, 0)  
        juego.jugar(1, 1)  
        juego.jugar(2, 0)  
        self.assertTrue(juego.juego_terminado())
        self.assertEqual(juego.ganador, "X")

    def test_ganar_diagonal(self):
        juego = Tateti()
        juego.jugar(0, 0)  
        juego.jugar(0, 1)  
        juego.jugar(1, 1)  
        juego.jugar(0, 2) 
        juego.jugar(2, 2) 
        self.assertTrue(juego.juego_terminado())
        self.assertEqual(juego.ganador, "X")


class TestTatetiMovimiento(unittest.TestCase):
    def setUp(self):
        self.juego = Tateti()
        self.juego.jugar(0,0); self.juego.jugar(1,0)   
        self.juego.jugar(0,2); self.juego.jugar(1,1)   
        self.juego.jugar(2,2); self.juego.jugar(2,0)   

    def test_movimiento_invalido_no_pierde_turno(self):
        self.juego.jugar(fila_destino=2, col_destino=0, fila_origen=1, col_origen=0)
        self.assertEqual(self.juego.jugador_actual, "X")  

    def test_mover_y_ganar(self):
        self.juego.jugar(fila_destino=0, col_destino=1, fila_origen=2, col_origen=2)
        self.assertTrue(self.juego.juego_terminado())
        self.assertEqual(self.juego.ganador, "X")


class TestCPU(unittest.TestCase):
    def test_cpu_coloca_ficha(self):
        juego = Tateti()
        juego.jugar(0,0) 
        juego.jugar_cpu()  
        self.assertEqual(juego.fichas_colocadas["O"], 1)


if __name__ == "__main__":
    unittest.main()
