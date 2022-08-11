
class CLIView:

    def mensaje(self, mensaje: str) -> None:
        print(mensaje)
    
    def obtener_posicion(self) -> str:
        posicion = " "
        while posicion not in list(map(str, range(1, 10))):
            posicion = input("Marcar posicion: ")
        return posicion

    def mostrar(self, tablero: object) -> None:
        print()
        print(f" {tablero['7']} | {tablero['8']} | {tablero['9']}")
        print("---+---+---")
        print(f" {tablero['4']} | {tablero['5']} | {tablero['6']}")
        print("---+---+---")
        print(f" {tablero['1']} | {tablero['2']} | {tablero['3']}")
        print()


class GUIView:
    pass
