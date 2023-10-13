from tkinter import *
from functools import partial
import os
from datetime import datetime
from tkinter import filedialog

class PrimerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Listado de archivos en un directorio")
        self.custName2 = StringVar()
        self.Label1 = Label(master, text="Vamos a seleccionar un directorio", width=50).grid(row=1, column=1)
        self.Boton1 = Button(master, text="Buscar...", command=self.directorio).grid(row=1, column=2)
        self.Entrada1 = Entry(master, textvariable=self.custName2, width=60).grid(row=2, columnspan=3)
        self.Boton2 = Button(master, text="Contenido de este directorio", command=self.contenido).grid(row=3, columnspan=3)
   
    def directorio(self):
        self.direct = filedialog.askdirectory(initialdir = "C:/", title="Seleccione un directorio") 
        self.custName2.set(self.direct)

    def contenido(self):
        direct2 = self.custName2.get()
        cont = os.listdir(direct2)
        for i in range(len(cont)):
            print (cont[i])

root = Tk()
root.geometry("800x200")
gui = PrimerGUI(root)
root.mainloop()