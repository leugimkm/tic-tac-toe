from tkinter import Tk
# pip install prototools
from prototools import main_loop


class TicTacToeCLI:

    def __init__(self, model: object, view: object) -> None:
        self.view = view()
        self.model = model(self.view)

    def _mainloop(self) -> None:
        self.model.reiniciar()
        while True:
            if self.model.game_over:
                self.view.mensaje("Game Over")
                break
            self.model.play(True)

    def run(self) -> None:
        main_loop(self._mainloop)


class TicTacToeGUI(Tk):

    def __init__(self, model: object, view: object):
        super().__init__()
        self._setup()
        self.view = view()
        self.view.pack(fill="both", expand=True)
        self.model = model(self.view)
        self._mainloop()

    def _setup(self):
        self.title("Tic Tac Toe")
        self.geometry("300x300")

    def _mainloop(self):
        if self.model.game_over:
            self.model.view.mensaje("Game Over")
            self.destroy()
        if self.view.obtener_posicion() is not None:
            self.model.play()
        self.after(100, self._mainloop)

    def reiniciar(self):
        self.model.reiniciar()
        self.view.reiniciar()
    
    def run(self):
        self.mainloop()
