from tkinter import *

lista = []

def guardar():
	print("GUARDAR")

def eliminar():
	print("ELIMINAR")

ventana = Tk()

# Variables
nombre = StringVar()
apellidoP = StringVar()
apellidoM = StringVar()
correo = StringVar()
telefono = StringVar()
conteliminar = StringVar()

# Colores
colorFondo = "#066"
colorLetra = "#FFF"

# Opciones de la ventana
ventana.title("Agenda de archivos")
ventana.geometry("700x500")
ventana.configure(background = colorFondo)

# Etiquetas, cajas de texto y botones
titulo = Label(ventana, text="Agenda de archivos", fg=colorLetra, bg=colorFondo).place(x=280,y=10)

labelNombre = Label(ventana, text="Nombre", bg=colorFondo, fg=colorLetra).place(x=50, y=60)
cajaNombre = Entry(ventana, textvariable = nombre).place(x=160, y=60)

labelApellidoP = Label(ventana, text="Apellido Paterno", bg=colorFondo, fg=colorLetra).place(x=50, y=100)
cajaApellidoP = Entry(ventana, textvariable = apellidoP).place(x=160, y=100)

labelApellidoM = Label(ventana, text="Apellido Materno", bg=colorFondo, fg=colorLetra).place(x=50, y=140)
cajaApellidoM = Entry(ventana, textvariable = apellidoM).place(x=160, y=140)

labelCorreo = Label(ventana, text="Correo", bg=colorFondo, fg=colorLetra).place(x=50, y=180)
cajaCorreo = Entry(ventana, textvariable = correo).place(x=160, y=180)

labelTelefono = Label(ventana, text="Telefono", bg=colorFondo, fg=colorLetra).place(x=50, y=220)
cajaTelefono = Entry(ventana, textvariable = telefono).place(x=160, y=220)

labelEliminar = Label(ventana, text="Telefono", bg=colorFondo, fg=colorLetra).place(x=370, y=60)
spinTelefono = Spinbox(ventana, textvariable=conteliminar).place(x=450,y=60)

btnGuardar = Button(ventana, text="GUARDAR", command=guardar, bg="#009", fg="white").place(x=180, y=260)

btnEliminar = Button(ventana, text="ELIMINAR", command=eliminar, bg="#009", fg="white").place(x=490, y=100)

mainloop()

