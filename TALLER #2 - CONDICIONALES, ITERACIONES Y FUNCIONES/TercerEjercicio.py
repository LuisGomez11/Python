horas = []
minutos = []
segundos = []
segundosTotales = []
precios = []

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

def pedirPrecioTarifa(mensaje):
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = float(input(mensaje))
            correcto = True
        except ValueError:
            print('Error, digite un numero entero')
    return num

def limitar(mensaje):
	correcto = False
	num = 0
	while(not correcto):
		try:
			num = int(input(mensaje))
			if num<=60:
				correcto = True
			else:
				print('Error, los minutos y segundos deben ser menor de 60')
		except ValueError:
			print('Error, digite un numero entero')
	return num

def mostrarTarifas(llamadasRealizadas):
	for i in range(llamadasRealizadas):
		print(f'La llamada {i+1} duro:')
		print(horas[i],' hora(s)')
		print(minutos[i],' minuto(s)')
		print(segundos[i],' segundo(s)')
		print('EN TOTAL FUERON: ',segundosTotales[i],' SEGUNDOS')
		print('Y EL COSTO TOTAL ES: $',precios[i])
		print('--------------------------------')

valorTarifa = pedirPrecioTarifa('Digite la tarifa por segundo: ')
llamadasRealizadas = pedirNumero('Digite el numero de llamadas realizadas: ')
print('-Digite la duracion de las llamadas en horas, minutos y segundos-')
print('--------------------------------')

for i in range(llamadasRealizadas):
	print(f'Duracion de la llamada {i+1}')
	hora = pedirNumero('Cuantas horas: ')
	horas.append(hora)
	minuto = limitar('Cuantos minutos: ')
	minutos.append(minuto)
	segundo = limitar('Cuantos segundos: ')
	segundos.append(segundo)
	total = (hora*3600)+(minuto*60)+segundo
	segundosTotales.append(total)
	precios.append(total*valorTarifa)
	print('--------------------------------')

print('----Duracion de cada llamada----')
print('--------------------------------')

mostrarTarifas(llamadasRealizadas)

print('FIN')