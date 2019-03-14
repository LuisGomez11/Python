def pedirNumeroInicio(mensaje):

    correcto = False
    num1 = 0
    while(not correcto):
        try:
            num1 = int(input(mensaje))
            correcto = True
        except ValueError:
            print('Error, digite un numero entero')
    return num1

numero1 = pedirNumeroInicio("Digite numero de inicio: ")

def pedirNumeroFinal(mensaje):

    correcto = False
    num2 = 0
    while(not correcto):
        try:
            num2 = int(input(mensaje))
            if num2 > numero1:
                correcto = True
            else:
                print('Error, digite un numero mayor al inicial')  
        except ValueError:
            print('Error, digite un numero entero')
    return num2

numero2 = pedirNumeroFinal("Digite numero final: ")

def numerosPares(numero1,numero2):
    for i in range(numero1,numero2,2):
        if numero1%2==1:
            print(i+1)
        else:
            print(i)

print('--Numeros pares del ',numero1,' al ',numero2,'--')

numerosPares(numero1,numero2)

print('-----Fin-----')