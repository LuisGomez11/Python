from io import open

archivo = open("texto.txt","r")

num = int(input('Cuantos numeros de bytes quieres leer: '))

print(archivo.read(num))

archivo.close()