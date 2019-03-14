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

listaFibonacci = []
listaPrimos = []

tam = pedirNumero('Digite el numero de datos que desea mostrar: ')

def fib(tam):
    a, b = 0,1
    while len(listaFibonacci) < tam:
        listaFibonacci.append(a)
        a, b = b, a+b

def validarPrimo(num):
	if num<2:
		return False
	for i in range(2,num):
		if num % i == 0:
			return False
	return True

def primos(tam):
    i = 0
    while len(listaPrimos) < tam:
        if validarPrimo(i) == True:
            listaPrimos.append(i)
        i += 1

fib(tam)   
primos(tam)

print('Lista primos:',listaPrimos)
print('Lista Fibonacci:',listaFibonacci)
