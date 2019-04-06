from io import open

archivo = open("texto2.txt","w")

num = int(input('Cuantas cadenas quiere escribir: '))

for i in range(num):
	cad = input('Ingrese una cadena: ')
	archivo.write(cad+'\n')

archivo.close()