lista = []

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
    cad = input('Ingrese una cadena de texto a la lista: ')
    lista.append(cad)
    con+=1

contador = 0

print('-------------------------------------------------')

cad_buscar = input('Ingrese la cadena que desea buscar en la lista: ')

for valor in lista:
    if valor==cad_buscar:
        contador+=1

print('-------------------------------------------------')

if contador==0:
    print('No se encontro la cadena en la lista')
else:
    print('Las veces que se encontro la cadena en la lista son: ',contador)
