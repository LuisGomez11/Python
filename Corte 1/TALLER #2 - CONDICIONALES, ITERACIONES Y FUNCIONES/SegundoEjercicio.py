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

numero = pedirNumero('Digite un numero: ')

def numerosTriangulares(num):
    sig = 0
    for i in range(1,num+1):
        sig = sig+i
        print(i,' --> ',sig)

numerosTriangulares(numero)