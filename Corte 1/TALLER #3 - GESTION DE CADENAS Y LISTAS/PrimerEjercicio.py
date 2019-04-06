cadena = input('Digite una cadena de texto: ')
caracter = input('Digite el caracter que desee buscar en la cadena: ')

def numVeces(cadena,caracter):
    contador=0
    for x in cadena:
        if x == caracter:
            contador+=1
    if contador==0:
        print("No se encuentra caracter en la cadena")
    print("Las veces que se encuentra son:",contador) 

numVeces(cadena,caracter)