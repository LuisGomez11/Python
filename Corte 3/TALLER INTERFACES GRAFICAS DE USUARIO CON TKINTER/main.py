from tkinter import *
from tkinter import messagebox

lista = []

def guardar():
	n = nombre.get()
	ap = apellidoP.get()
	am = apellidoM.get()
	c = correo.get()
	t = telefono.get()
	lista.append(n+"$"+ap+"$"+am+"$"+t+"$"+c)
	escribirContacto()
	messagebox.showinfo("Guardado","El contacto ha sido guardado en la agenda")
	nombre.set("")
	apellidoP.set("")
	apellidoM.set("")
	correo.set("")
	telefono.set("")
	consultar()

def eliminar():
	eliminado = conteliminar.get()
	removido = False
	for elemento in lista:
		arreglo = elemento.split("$")
		if conteliminar.get() == arreglo[3]:
			lista.remove(elemento)
			removido = True
	escribirContacto()
	consultar()
	if removido:
		messagebox.showinfo("Eliminar","Elemento eliminado "+eliminado)

def consultar():
	r = Text(ventana, width=80, height=15)
	lista.sort()
	valores = []
	r.insert(INSERT, "Nombre\tApellido Pa\t\tApellido Ma\t\tTeléfono\t\tCorreo\n")
	for elemento in lista:
		arreglo = elemento.split("$")
		valores.append(arreglo[3])
		r.insert(INSERT, arreglo[0]+"\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
	r.place(x=20,y=350)
	spinTelefono = Spinbox(ventana, textvariable=conteliminar).place(x=450,y=60)
	if lista == []:
		spinTelefono = Spinbox(ventana, textvariable=conteliminar).place(x=450,y=60)
	r.config(state=DISABLED)

def iniciarArchivo():
 	archivo = open("ag.txt","a")
 	archivo.close()

def cargar():
	archivo = open("ag.txt","r")
	linea = archivo.readline()
	if linea:
		while linea:
			if linea[-1]=='\n':
				linea = linea[:-1]
			lista.append(linea)
			linea = archivo.readline()
	archivo.close()

def escribirContacto():
	archivo = open("ag.txt","w")
	lista.sort()
	for elemento in lista:
		archivo.write(elemento+"\n")
	archivo.close()


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

iniciarArchivo()
cargar()
consultar()

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

