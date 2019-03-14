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

print('---------------------------------------------------------------')

con = 0

listaNumeros = []

while con<tam:
    num = pedirNumero('Ingrese un numero a la lista: ')
    listaNumeros.append(num)
    con+=1

suma = 0
pruducto = 1
mayor = listaNumeros[0]
menor = listaNumeros[0]

for i in listaNumeros:
    suma+=i
    pruducto*=i
    
tam = len(listaNumeros)

for i in range(tam):
    if(menor>listaNumeros[i]):
        menor=listaNumeros[i]
    if(mayor<listaNumeros[i]):
        mayor=listaNumeros[i]

print('---------------------------------------------------------------')
print('La lista es:',listaNumeros)
print('---------------------------------------------------------------')
print('La suma de todos los numeros de la lista es:',suma)
print('---------------------------------------------------------------')
print('El producto de todos los numeros de la lista es:',pruducto)
print('---------------------------------------------------------------')
print('El numero mayor de la lista es:',mayor)
print('---------------------------------------------------------------')
print('El numero menor de la lista es:',menor)