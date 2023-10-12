from tkinter import *

root= Tk()

root.title("Esta es mi primera ventana")
root.columnconfigure(0, weight=1)
root.rowconfigure(4, weight=1)

etiqueta1 = Label(root, text="Primeros pasos con Tkinter").grid(row=0, column= 0, pady=2)
etiqueta2 = Label(root, text=". . . pero esto esta muy vacio, no? ").grid(row=1, column = 0, pady=2)

boton1 = Button(root, text="Minimizar", command=root.iconify).grid(row=2, column = 0, sticky= E+W, pady=2)
boton2 = Button(root, text="Donde estamos?", command=root.destroy).grid(row=3, column = 0, sticky= E+W, pady=2)

root.geometry("400x150")

root.mainloop()
