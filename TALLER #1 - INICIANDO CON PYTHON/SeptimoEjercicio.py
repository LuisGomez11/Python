print('---Factorial de un numero---')
numero = int(input('Digite un numero: '))
con = 1
resultado=1
while con<numero+1:
    resultado *=con
    con+=1
print(resultado)