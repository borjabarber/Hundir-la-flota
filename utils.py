import numpy as np
import random

def crear_tablero(tamano=10):
    return np.full((tamano, tamano), "_")

def colocar_barco(barco, tablero):
    for casilla in barco:
        fila, columna = casilla
        tablero[fila, columna] = "O"

def disparar(casilla, tablero):
    fila, columna = casilla
    if tablero[fila, columna] == "O":
        tablero[fila, columna] = "X"
        return "Tocado"
    else:
        tablero[fila, columna] = "A"
        return "Agua"

def crear_barco(eslora, tamano_tablero=10):
    orientacion = random.choice(["horizontal", "vertical"])
    if orientacion == "horizontal":
        fila = random.randint(0, tamano_tablero - 1)
        columna_inicial = random.randint(0, tamano_tablero - eslora)
        barco = [(fila, columna_inicial + i) for i in range(eslora)]
    else:
        fila_inicial = random.randint(0, tamano_tablero - eslora)
        columna = random.randint(0, tamano_tablero - 1)
        barco = [(fila_inicial + i, columna) for i in range(eslora)]
    return barco

def puede_colocar_barco(barco, tablero):
    for casilla in barco:
        fila, columna = casilla
        if tablero[fila, columna] != "_":
            return False
    return True

def colocar_barcos(tablero, tamano_tablero=10):
    barcos = []
    barcos.extend([crear_barco(2, tamano_tablero) for _ in range(3)])
    barcos.extend([crear_barco(3, tamano_tablero) for _ in range(2)])
    barcos.append(crear_barco(4, tamano_tablero))

    for barco in barcos:
        while not puede_colocar_barco(barco, tablero):
            barco = crear_barco(len(barco), tamano_tablero)
        colocar_barco(barco, tablero)