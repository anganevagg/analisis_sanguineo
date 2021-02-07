from tkinter import *

from analisis import *

class GS6(Analysis):
	def __init__(self, root):
		self._root=root
		self.title = "Análisis sanguineo 6"
		self.entries=["Glucosa", "Ácido úrico", "Colesterol", "Urea", "Triglicéridos", "Creatinina"]
		
