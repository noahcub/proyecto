from tkinter import *
import tkinter.messagebox

class PrimerGUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI con botones de radio")
        self.num1 = StringVar()
        self.num2 = StringVar()
        self.radio = IntVar()
        self.etiqueta1 = Label(master, text="Primer numero: ").place(x=20, y=20)
        self.caja1 = Entry(master, textvariable=self.num1).place(x=170, y=20)
        self.etiqueta2 = Label(master, text="Segundo numero: ").place(x=20, y=50)
        self.caja2 = Entry(master, textvariable=self.num2).place(x=170, y=50)
        self.etiqueta3 = Label(master, text="Operacion que se desea realizar: ").place(x=20, y=80)

        self.suma = Radiobutton(master, text="+", value=1, variable=self.radio).place(x=20, y=110)
        self.resta = Radiobutton(master, text="-", value=2, variable=self.radio).place(x=120, y=110)
        self.multi = Radiobutton(master, text="x", value=3, variable=self.radio).place(x=20, y=140)
        self.div = Radiobutton(master, text="/", value=4, variable=self.radio).place(x=120, y=140)
    
        self.boton = Button(master, text="Calcular la operación", command=self.operacion).place(x=60, y=180)

    def operacion(self):
        self.n1 = float(self.num1.get())
        self.n2 = float(self.num2.get())
#        resultado = 0
        if self.radio.get() == 1:
            resultado= self.n1+self.n2
        if self.radio.get() == 2:
            resultado= self.n1-self.n2
        if self.radio.get() == 3:
            resultado= self.n1*self.n2
        if self.radio.get() == 4:
            resultado= self.n1/self.n2

        tkinter.messagebox.showinfo ("Calculo Finalizado", "El resultado es: "+ str(resultado))

root = Tk()
root.geometry("400x250")
gui = PrimerGUI(root)
root.mainloop()