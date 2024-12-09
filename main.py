from utils import *

tamano_tablero = 10

tablero_jugador = crear_tablero(tamano_tablero)
colocar_barcos(tablero_jugador)

tablero_skynet = crear_tablero(tamano_tablero)
colocar_barcos(tablero_skynet)

barcos_restantes_jugador = True
barcos_restantes_skynet = True

turno_actual = 1
turnos_totales = 10

while barcos_restantes_jugador and barcos_restantes_skynet and turno_actual <= turnos_totales:
    print("Turno" ,turno_actual, "/" ,turnos_totales)

    print("Tu tablero")
    print(tablero_jugador)

    disparo_valido = False
    while not disparo_valido:
        casilla = input("Introduce las coordenadas de tu disparo (fila y columna): ")
        try:
            fila, columna = map(int, casilla.split(","))
            if 0 <= fila < tamano_tablero and 0 <= columna < tamano_tablero:
                disparo_valido = True
            else:
                print("Señor, Cordenadas fuera del rango del tablero. Intenta nuevamente.")
        except ValueError:
            print("Señor, asegúrese de introducir números separados por una coma. Intenta nuevamente.")
    
    resultado = disparar((fila, columna), tablero_skynet)
    print(resultado)

    # Verificar si quedan barcos en el tablero de la máquina
    barcos_restantes_skynet = np.any(tablero_skynet == "O")
    if not barcos_restantes_skynet:
        print("Has salvado el futuro")
        break

    # Imprimir los disparos de la máquina
    fila_skynet = random.randint(0, tamano_tablero - 1)
    columna_skynet = random.randint(0, tamano_tablero - 1)
    resultado_skynet = disparar((fila_skynet, columna_skynet), tablero_jugador)
    print(f"el T-1000 ha ordenado un disparo en ({fila_skynet}, {columna_skynet}): {resultado_skynet}")

    # Verificar si quedan barcos en el tablero del jugador
    barcos_restantes_jugador = np.any(tablero_jugador == "O")
    if not barcos_restantes_jugador:
        print("Jhon Connor ha muerto")
        break

    turno_actual += 1

if turno_actual > turnos_totales:
    print("Ha explotado una bomba nucelar. El juego ha terminado.")