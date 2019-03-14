def conventir_a_Dolares(pesos):
	dolares = pesos*0.00032
	print('Pesos colombianos a dolares')
	print(pesos," -> ",dolares)

def conventir_a_Euros(pesos):
	euros = pesos*0.00028
	print('Pesos colombianos a euros')
	print(pesos," -> ",euros)

def conventir_a_Bitcoins(pesos):
	bitcoins = pesos*0.860784
	print('Pesos colombianos a bitcoins')
	print(pesos," -> ",bitcoins)

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

pesos = pedirNumero('Digite una cifra en pesos colombianos: ')

conventir_a_Dolares(pesos)
conventir_a_Euros(pesos)
conventir_a_Bitcoins(pesos)