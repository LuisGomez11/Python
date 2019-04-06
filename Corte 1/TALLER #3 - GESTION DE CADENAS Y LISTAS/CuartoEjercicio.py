
lista = []
lista_unicos = []
lista_duplicados = []

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

tam = pedirNumero('Digite el numero de datos que ingresara: ')

print('-------------------------------------------------')

con = 0

while con<tam:
    num = pedirNumero('Ingrese un numero a la lista: ')
    lista.append(num)
    con+=1

num_repe = 0

for valor in lista:
    if valor in lista_unicos:
        lista_unicos.remove(valor)
        num_repe = valor
    elif num_repe == valor:
        continue
    else:
        lista_unicos.append(valor)

for valor in lista:
    if valor in lista_unicos:
        continue
    if valor in lista_duplicados:
        continue
    lista_duplicados.append(valor)


print('-------------------------------------------------')

print('Lista:',lista)
print('Lista con los elementos unicos:',lista_unicos)
print('Lista con los elementos duplicados:',lista_duplicados)
