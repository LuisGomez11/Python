cadena = input('Digite una cadena de texto: ')

def numVeces(cadena):
    contador = 0
    for vocal in cadena:
        if (vocal.upper()=='A' or vocal.upper()=='E' or vocal.upper()=='I' or vocal.upper()=='O' or vocal.upper()=='U'):
            contador+=1
    if contador==0:
        print("No se encuentra volcales en la cadena")
    print("Las veces que se encuentra una vocal en la cadena son:",contador)

numVeces(cadena)