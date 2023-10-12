from tkinter import *

class PrimerGUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI con botones de radio")
        self.idanimal = IntVar()
        self.etiqueta2 = Label(master, text="Animal doméstico preferido ").place(x=120, y=10)
        self.botonperro = Radiobutton(master, text='Perro', value=1, variable=self.idanimal).place(x=70, y=30)
        self.botongato = Radiobutton(master, text='Gato', value=2, variable=self.idanimal).place(x=160, y=30)
        self.botonpeces = Radiobutton(master, text='Peces', value=3, variable=self.idanimal).place(x=250, y=30)
        self.botonotros = Radiobutton(master, text='Otros', value=4, variable=self.idanimal).place(x=340, y=30)
               
        self.idcolor = IntVar()
        self.botonrojo = Radiobutton(master, text="Rojo", value=1, variable=self.idcolor).place(x=70, y=70)
        self.botonverde = Radiobutton(master, text="Verde", value=2, variable=self.idcolor).place(x=160, y=70)
        self.botonazul = Radiobutton(master, text="Azul", value=3, variable=self.idcolor).place(x=250, y=70)
        self.botonamarillo = Radiobutton(master, text="Amarillo", value=4, variable=self.idcolor).place(x=340, y=70)
        self.boton = Button(master, text="Sus gustos son...", command=self.imprimir).place(x=160, y=110)
    
    def imprimir(self):
        animal = self.idanimal.get()
        color = self.idcolor.get()
        if animal == 1.0:
            animal = "perro"
        elif animal == 2.0:
            animal = "gato"
        elif animal == 3.0:
            animal = "peces"
        else:
            animal = "otros"
        
        if color == 1.0:
            color = "rojo"
        elif color == 2.0:
            color = "verde"
        elif color == 3.0:
            color = "azul"
        else:
            color = "amarillo"
        print ('Su animal favorito es: ', animal, '\nY su color favorito es:', color)

root = Tk()
root.geometry("500x200")
gui = PrimerGUI(root)
root.mainloop()