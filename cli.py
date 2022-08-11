# pip install prototools
from prototools import main_loop
from models import Game
from views import CLIView


class TicTacToe:

    def __init__(self):
        self.game = Game(CLIView())

    def _mainloop(self):
        self.game.reiniciar()
        while not self.game.game_over:
            self.game.play(True)

    def mainloop(self):
        main_loop(self._mainloop)


if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.mainloop()
