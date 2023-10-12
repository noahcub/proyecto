from tkinter import *

class PrimerGUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI con cuadros de entrada")
        self.nombre = StringVar()
        #self.nombre.set("Escriba su nombre")
        self.ape1 = StringVar()
        #self.ape1.set("Primer apellido")
        self.ape2 = StringVar()
        #self.ape2.set("Segundo apellido")
        self.dni = StringVar()
        #self.dni.set("00000000")

        self.etiqueta0 = Label(master, text="Introduzca sus datos personales", justify=CENTER).grid(row=0, columnspan=3)
        self.etiqueta1 = Label(master, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
        self.nombreInput = Entry(master, textvariable=self.nombre).grid(row=1, column=2)
        self.etiqueta2 = Label(master, text="Primer apellido").grid(row=2, column=0, padx=5, pady=5)
        self.ape1Input = Entry(master, textvariable=self.ape1).grid(row=2, column=2, padx=5, pady=5)
        self.etiqqeta3 = Label(master, text="Segundo apellido").grid(row=3, column=0, padx=5, pady=5)
        self.ape2Input = Entry(master, textvariable=self.ape2).grid(row=3, column=2, padx=5, pady=5)
        self.etiqueta4 = Label(master, text="DNI").grid(row=4, column=0, padx=5, pady=5)
        self.dniInput = Entry(master, textvariable=self.dni).grid(row=4, column=2, padx=5, pady=5)
        self.boton = Button(master, text="Bienvenido", command=self.saludo).grid(row=5, columnspan=3, padx=5, pady=5)

    def saludo(self):
        print ("Bienvenido al curso Python: "+self.nombre.get()+" "+self.ape1.get()+" "+self.ape2.get()+", con DNI "+self.dni.get()+". Esperamos que este curso le sea de utilidad")

root = Tk()
root.geometry("400x250")
gui = PrimerGUI(root)
root.mainloop()