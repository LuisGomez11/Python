listaOriginal = []
listaConCaracteres = []

def pedirNumero(mensaje):
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input(mensaje))
            correcto = True
        except ValueError:
            print('Error, digite un numero entero')
    return num

def pedirCaracter(mensaje):
	correcto = False
	caracter = ''
	while (not correcto):
		try:
			caracter = input(mensaje)
			if len(caracter) == 1:
				correcto = True
			else :
				print('Error, digite un caracter')
		except Exception:
			print('Error, digite un caracter')
	return caracter

tam = pedirNumero('Digite el numero de datos que ingresara: ')

print('----------------------------------------------')

con = 0

while con<tam:
    cad = input('Ingrese una cadena de texto a la lista: ')
    listaOriginal.append(cad)
    con+=1

print('----------------------------------------------')

car = pedirCaracter('Digite un caracter: ')

for valor in listaOriginal:
	listaConCaracteres.append(car)
	listaConCaracteres.append(valor)

print('----------------------------------------------')
print('Lista original:',listaOriginal)
print('Lista con caracter:',listaConCaracteres)