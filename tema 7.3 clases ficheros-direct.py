from tkinter import *
from tkinter import filedialog as tkf
from functools import partial
import os
from datetime import datetime

class PrimerGUI:
    def __init__(self, master):
        self.custName2 = StringVar()
        self.master = master
        master.title("Informacion de un fichero")
        self.Name1 = Label(master, text = "Vamos a obtener informacion de un fichero de tu ordenador", width=100).grid(row=1, column=6)
        self.Entrada1 = Entry(master, text=self.custName2, width=60).grid(row=5, column=6)
        self.Boton1 = Button(master, text="Seleccion de archivo", command=self.fichero).grid(row=3, column = 6)
        self.Boton2 = Button(master, text="Info del archivo", command=self.info).grid(row=7, column=6)
   
    def fichero(self):
        fsave = tkf.askopenfilename(initialdir = "C:/", title="Selecciona el fichero", filetypes=(("txt files", "*.txt"),("jpeg files", "*.jpg"),("all files", "*.*"))) 
        if len (fsave) != 0:
            self.fsave = fsave
            print (fsave)
            self.custName2.set(str(fsave))
            root.update_idletasks()
    
    def info(self):
            print ('El fichero ocupa ', os.path.getsize(self.fsave)/1024, 'KB')
            print ('Fecha de creacion ', datetime.fromtimestamp(os.path.getctime(self.fsave)).strftime('%Y-%m-%d %H:%M:%S'))
            print ('Fecha de modificacion ', datetime.fromtimestamp(os.path.getmtime(self.fsave)).strftime('%Y-%m-%d %H:%M:%S'))

root = Tk()
root.geometry("1000x200")
gui = PrimerGUI(root)
root.mainloop()