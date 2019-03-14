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

lista1 = []
lista2 = []

tam = pedirNumero('Digite el numero de datos que ingresara: ')

print('-----------------------------------------')

con = 0

while con<tam:
    num = pedirNumero('Ingrese un numero a la lista 1: ')
    lista1.append(num)
    con+=1


print('-----------------------------------------')

for i in lista1:
    valor = i+1
    lista2.append(valor)

print('Primera lista:',lista1)
print('Segunda lista:',lista2)