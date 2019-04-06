cadena = input('Digite una cadena de texto: ')

def impDosPrimerosCar(cadena):
    print('Primeros dos caracteres:',cadena[0:2])
def impTresPrimerosCar(cadena):
    print('Primeros tres caracteres:',cadena[0:3])
def impCadaDosCar(cadena):
    print('Cada dos caracteres',cadena[::2])
def impCadenaInv(cadena):
    print('Invertida:',cadena[::-1])

impDosPrimerosCar(cadena)
impTresPrimerosCar(cadena)
impCadaDosCar(cadena)
impCadenaInv(cadena)
