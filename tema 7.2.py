from tkinter import *

root= Tk()

root.title("Esta es mi primera ventana")
label1 = Label(root, text="Primeros pasos con Tkinter").place(x=140, y=15)
label2 = Label(root, text=". . . pero esto esta muy vacio, no?").place(x=110, y = 45)

boton1 = Button(root, text="Aceptar").place(x=175, y=75)

root.geometry("500x120")

root.mainloop()