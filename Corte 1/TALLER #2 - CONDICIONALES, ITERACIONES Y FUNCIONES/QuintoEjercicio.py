def mostarDatos(menor,medio,mayor):
    print("1. ",menor)
    print("2. ",medio)
    print("3. ",mayor)

def organizarAscendente(num1, num2, num3):
    
    if ((num1<=num2) and (num1<=num3)):
        
        menor = num1

        if(num2 <= num3):
            medio = num2
            mayor = num3
        else:
            medio = num3
            mayor = num2

        mostarDatos(menor,medio,mayor)

    elif((num2<=num1) and (num2<=num3)):
        
        menor = num2

        if(num1 <= num3):
            medio = num1
            mayor = num3
        else:
            medio = num3
            mayor = num1

        mostarDatos(menor,medio,mayor)

    else:

        menor = num3

        if(num1 <= num2):
            medio = num1
            mayor = num2
        else:
            medio = num2
            mayor = num1

        mostarDatos(menor,medio,mayor)

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

numero1 = pedirNumero('Digite primer numero: ')
numero2 = pedirNumero('Digite segundo numero: ')
numero3 = pedirNumero('Digite tercer numero: ')

organizarAscendente(numero1,numero2,numero3)

print('FIN')