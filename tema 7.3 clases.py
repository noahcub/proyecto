from tkinter import *

class PrimerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Un GUI muy simple")
        master.label1 = Label(master, text="Primeros pasos con Tkinter")
        master.label1.pack()
        master.label2 = Label(master, text=". . . pero esto esta muy vacio, no?")
        master.label2.pack()
        master.boton1 = Button(master, text="Aceptar")
        master.boton1.pack()

root = Tk()
root.geometry("400x100")
PrimerGUI(root)
root.mainloop()