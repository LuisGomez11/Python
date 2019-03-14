lista1 = []
lista2 = []
listaSolicitada = []


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

tam = pedirNumero('Digite el numero de datos que ingresara a la primera lista: ')

print('--------------------------------------------------------------------')

con = 0

while con<tam:
    num = pedirNumero('Ingrese un numero a la lista 1: ')
    lista1.append(num)
    con+=1

print('--------------------------------------------------------------------')

tam2 = pedirNumero('Digite el numero de datos que ingresara a la segunda lista: ')

print('--------------------------------------------------------------------')

con2 = 0

while con2<tam2:
    num = pedirNumero('Ingrese un numero a la lista 2: ')
    lista2.append(num)
    con2+=1

print('--------------------------------------------------------------------')

for i in lista1:
	listaSolicitada.append(i)

listaSolicitada.pop()

for i in lista2:
	listaSolicitada.append(i)

print('Primera lista:',lista1)
print('Segunda lista:',lista2)
print('Lista solicitada:',listaSolicitada)