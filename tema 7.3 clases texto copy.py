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
        self.nombreInput = Text(master, height=1, width=10)
        self.nombreInput.grid(row=1, column=2)
        self.etiqueta2 = Label(master, text="Primer apellido").grid(row=2, column=0, padx=5, pady=5)
        self.ape1Input = Text(master, height=1, width=10)
        self.ape1Input.grid(row=2, column=2)
        self.etiqqeta3 = Label(master, text="Segundo apellido").grid(row=3, column=0, padx=5, pady=5)
        self.ape2Input = Text(master, height=1, width=10)
        self.ape2Input.grid(row=3, column=2)
        self.etiqueta4 = Label(master, text="DNI").grid(row=4, column=0, padx=5, pady=5)
        self.dniInput = Text(master, height=1, width=10)
        self.dniInput.grid(row=4, column=2)
        self.boton = Button(master, text="Bienvenido", command=self.saludo).grid(row=5, columnspan=3, padx=5, pady=5)

    def saludo(self):
        nombre = self.nombreInput.get("1.0", 'end-1c')
        ape1 = self.ape1Input.get("1.0", 'end-1c')
        ape2 = self.ape2Input.get("1.0", 'end-1c')
        dni = self.dniInput.get("1.0", 'end-1c')
        print ("Bienvenido al curso Python: "+nombre+" "+ape1+" "+ape2+" con DNI "+ dni +". Esperamos que este curso le sea de utilidad")

root = Tk()
root.geometry("400x250")
gui = PrimerGUI(root)
root.mainloop()