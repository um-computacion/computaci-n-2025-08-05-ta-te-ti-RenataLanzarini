# 🎮 Proyecto Final – Tateti Dinámico en Python

Este trabajo práctico es el **proyecto final de la materia Computación 1**.  
La idea fue programar una versión diferente del clásico *Tateti (Tic-Tac-Toe)* usando **Python** con **Programación Orientada a Objetos (POO)** y pruebas con **unittest**.

Lo distinto de este Tateti es que no termina cuando se llena el tablero, sino que cada jugador tiene solo **tres fichas** y, una vez colocadas, las debe ir **moviendo** hasta lograr la victoria.

---

## 👩‍🎓 Alumno
- **Nombre:** María Renata Lanzarini  
- **Carrera:** Ingeniería en Informática  
- **Materia:** Computación 1 – Universidad de Mendoza  
- **Año:** 2025  

---

## 📜 Reglas del juego

- Juegan dos: **X** y **O**.  
- Siempre empieza **X**.  
- Cada jugador tiene **3 fichas como máximo en el tablero**.  
- **Fase 1:** Colocación → se ponen fichas en casillas vacías hasta llegar a 3.  
- **Fase 2:** Movimiento → cuando un jugador ya tiene 3, debe mover una ficha suya a otra casilla vacía.  
- **Ganador:** el primero que alinee sus 3 fichas en fila, columna o diagonal.  
- Si intentás poner en un lugar ocupado o mover la ficha del otro, el turno **no se pierde**, simplemente se muestra un error y podés volver a jugar.  

---

## 📂 Estructura del proyecto

Tateti/
│
├── cli.py → Código para jugar por consola
├── jugador.py → Clase Jugador (guarda el símbolo X u O)
├── tablero.py → Clase Tablero (maneja el tablero y validaciones)
├── tateti.py → Clase principal con las reglas del juego
│
└── tests/ → Carpeta con los tests
└── test_tateti.py → Pruebas con unittest

## ▶️ Cómo ejecutar el juego


1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/um-computacion/computaci-n-2025-08-05-ta-te-ti-RenataLanzarini.git
   cd computaci-n-2025-08-05-ta-te-ti-RenataLanzarini

2. Ejecutar el juego:

python3 cli.py


3. Para salir en cualquier momento, escribir q.

## 🧪 Tests

El proyecto usa el módulo estándar unittest para probar la lógica del juego.

Para correr todos los tests:
python3 -m unittest discover -s tests -p "test_*.py" -v

