from tkinter import *

class PrimerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Un GUI muy simple")
        self.label = Label(master, text="Este es mi primer GUI con botones").place(x=10, y=30)
        self.boton1 = Button(master, text="Minimizar", command=self.minimizar).place(x=10, y=60)
        self.boton2 = Button(master, text="Donde estoy?", command=self.imprimir, bg="green", fg="yellow").place(x=10, y=90)
    
    def imprimir(self):
        print ("Esta usted en el curso Python")
    
    def minimizar(self):
        self.master.iconify()

root = Tk()
root.geometry("400x200")
PrimerGUI(root)
root.mainloop()