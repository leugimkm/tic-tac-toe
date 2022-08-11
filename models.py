from dataclasses import dataclass
from typing import Dict


@dataclass
class Jugador:
    simbolo: str = "X"
    color: str = "blue"

    def cambiar(self) -> None:
        self.simbolo = "O" if self.simbolo == "X" else "X"
        self.color = "red" if self.color == "blue" else "blue"


class Tablero:

    def __init__(self) -> None:
        self._t: Dict[str, str] = {str(n): " " for n in range(1, 10)}

    @property
    def tablero(self) -> Dict[str, str]:
        return self._t

    def esta_vacio(self, posicion) -> bool:
        return self._t[posicion] == " "

    def es_tres_en_linea(self, jugador: str) -> bool:
        return (
            (self._t["1"] == self._t["2"] == self._t["3"] == jugador) or
            (self._t["4"] == self._t["5"] == self._t["6"] == jugador) or
            (self._t["7"] == self._t["8"] == self._t["9"] == jugador) or
            (self._t["1"] == self._t["4"] == self._t["7"] == jugador) or
            (self._t["2"] == self._t["5"] == self._t["8"] == jugador) or
            (self._t["3"] == self._t["6"] == self._t["9"] == jugador) or
            (self._t["1"] == self._t["5"] == self._t["9"] == jugador) or
            (self._t["3"] == self._t["5"] == self._t["7"] == jugador)
        )

    def marcar(self, posicion, jugador: str) -> None:
        self._t[posicion] = jugador

    def reiniciar(self) -> None:
        for k in self._t:
            self._t[k] = " "    


class Game:

    def __init__(self, view) -> None:
        self.tablero = Tablero()
        self.jugador = Jugador()
        self.view = view
        self.game_over = False
        self.rondas = 0

    def play(self, show: bool = False) -> None:
        if show:
            self.view.mostrar(self.tablero.tablero)
        posicion = self.view.obtener_posicion()
        if self.tablero.esta_vacio(posicion):
            self.tablero.marcar(posicion, self.jugador.simbolo)
            if self.tablero.es_tres_en_linea(self.jugador.simbolo):
                self.game_over = True
                if show:
                    self.view.mostrar(self.tablero.tablero)
                self.view.mensaje(f"Ganador: {self.jugador.simbolo}")
            self.jugador.cambiar()
            self.rondas += 1
            if self.rondas == 9 and not self.game_over:
                self.game_over = True
                if show:
                    self.view.mostrar(self.tablero.tablero)
                self.view.mensaje("Empate")
        else:
            self.view.mensaje("Posicion ocupada")

    def reiniciar(self):
        self.tablero.reiniciar()
        self.rondas = 0
        self.game_over = False
