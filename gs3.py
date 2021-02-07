from tkinter import *

from analisis import *

class GS3(Analysis):
	def __init__(self, root):
		self._root=root
		self.title = "Análisis sanguineo 3"
		self.entries=["Glucosa", "Ácido úrico", "Colesterol"]
		