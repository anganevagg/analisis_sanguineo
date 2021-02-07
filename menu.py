from tkinter import *

from gs3 import GS3
from gs6 import GS6


class Menu:
    def __init__(self, options):
        self.__options=options
        self.window = Tk()
        self.window.title("LABORATORIO DE ANÁLISIS CLÍNICIOS DM")
        self.window.geometry("640x480")
        self.window.resizable(0,0)
        msg = Label(self.window, text="Elija el tipo de estudio a realizar", font=("comic sans", 18)).place(x=100, y=50)
        operations = [GS3(self.window) ,GS6(self.window)]
        for option in range(len(options)):
            Button(self.window, text=options[option], command=operations[option].show).place(x=200, y=100+(50*option))
        self.window.mainloop()