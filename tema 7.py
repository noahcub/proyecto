from tkinter import *

root= Tk()

root.title("Esta es mi primera ventana")
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

etiqueta1 = Label(root, text="Primeros pasos con Tkinter").grid(row=0, column= 0, pady=2)
etiqueta2 = Label(root, text=". . . pero esto esta muy vacio, no? ").grid(row=1, column = 0, pady=2)

boton1 = Button(root, text="Aceptar").grid(row=2, column = 0, sticky= E+W, pady=2)

root.geometry("400x100")

root.mainloop()
