from tkinter import *

class Analysis:
	def show(self):
		self.__window=Toplevel(self._root)
		self.__window.geometry("480x480")
		self.__window.resizable(0,0)
		self.values = []
		for i in range(len(self.entries)):
			self.values.append(DoubleVar())
		Label(self.__window, text=self.title, font=("comic sans", 16)).place(x=120, y=0)
		for entry in range(len(self.entries)):
			Label(self.__window, text=self.entries[entry]).place(x=20, y=30+(60*entry))
			Entry(self.__window, textvariable=self.values[entry]).place(x=20, y=60+(60*entry))
			Label(self.__window, text="mmol/L").place(x=180,y=60+(60*entry))
		Button(self.__window, text="Convertir", command=self.convert).place(x=180, y=420)
	def convert(self):
		conversions = [18.02, 0.02, 380.66, 6.01, 87.5, 0.01]
		for value in range(len(self.values)):
			Label(self.__window, text=f"{self.values[value].get()*conversions[value]} mg/dL").place(x=280, y=60+(60*value))