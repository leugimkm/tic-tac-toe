from typing import Dict

Tablero = Dict[str, str]
ANCHO = 47


def instrucciones() -> None:
    print(f" Tic-Tac-Toe ".center(ANCHO, "="))
    print("\nPosiciones del tablero: ")
    print(" 7 | 8 | 9\n---+---+---")
    print(" 4 | 5 | 6\n---+---+---")
    print(" 1 | 2 | 3\n")
    input('Presiona "ENTER" para empezar...')


def mostrar(tablero: Tablero) -> None:
    print()
    print(f" {tablero['7']} | {tablero['8']} | {tablero['9']}")
    print("---+---+---")
    print(f" {tablero['4']} | {tablero['5']} | {tablero['6']}")
    print("---+---+---")
    print(f" {tablero['1']} | {tablero['2']} | {tablero['3']}")
    print()


def resultado(tablero: Tablero, jugador: str = None) -> None:
    mostrar(tablero)
    if jugador is None:
        print(" Empate ".center(47, "="))
    else:
        print(f' El jugador "{jugador}" gano '.center(47, "="))


def es_tres_en_linea(jugador: str, tablero: Tablero) -> bool:
    return (
        (tablero["1"] == tablero["2"] == tablero["3"] == jugador) or
        (tablero["4"] == tablero["5"] == tablero["6"] == jugador) or
        (tablero["7"] == tablero["8"] == tablero["9"] == jugador) or
        (tablero["1"] == tablero["4"] == tablero["7"] == jugador) or
        (tablero["2"] == tablero["5"] == tablero["8"] == jugador) or
        (tablero["3"] == tablero["6"] == tablero["9"] == jugador) or
        (tablero["1"] == tablero["5"] == tablero["9"] == jugador) or
        (tablero["3"] == tablero["5"] == tablero["7"] == jugador)
    )


def obtener_posicion(jugador: str) -> str:
    posicion = " "
    while posicion not in list(map(str, range(1, 10))):
        posicion = input(f"Marcar {jugador} en: ")
    return posicion


def jugar() -> None:
    instrucciones()
    tablero: Tablero = {str(n): " " for n in range(1, 10)}
    jugador = "X"
    ronda = 0
    while ronda <= 9:
        mostrar(tablero)
        posicion = obtener_posicion(jugador)
        if tablero[posicion] == " ":
            tablero[posicion] = jugador
            ronda += 1
        else:
            print("Posicion ocupada")
            continue
        if ronda >= 5:
            if es_tres_en_linea(jugador, tablero):
                resultado(tablero, jugador)
                break
        if ronda == 9:
            resultado(tablero)
            break
        jugador = "O" if jugador == "X" else "X"


def main():
    while True:
        jugar()
        print('Jugar otra vez? "S" o "N"')
        if not input("> ").lower().startswith("s"):
            break


if __name__ == "__main__":
    main()
