from io import open
import os

def escribir():
    os.system('cls')
    archivo = open("contactos.txt","a")
    print('')
    print('Ingrese los datos del contacto'.center(50, "="))
    print('')
    nombre = input('Digite nombre: ')
    telefono = input('Digite telefono: ')
    email = input('Digite email: ')
    archivo.write(nombre+', '+telefono+', '+email+'\n')
    archivo.close()

def leer():
    os.system('cls')
    archivo = open("contactos.txt","r")
    print('')
    print('Contactos'.center(50, "="))
    print('')
    print(archivo.read())
    input('Presione ENTER para continuar')
    archivo.close()

while True:
    os.system('cls')
    print('')
    print('Menu'.center(50, "="))
    print('')
    print('1. Guardar Contacto')
    print('2. Leer Contactos')
    print('3. Salir')
    print('')
    opc = input('Digite una opcion: ')
    
    if opc == '1':
        escribir()
    elif opc == '2':
        leer()
    elif opc == '3':
        os.system('cls')
        break
    else:
        print('')
        print('Digite una opcion correcta')
        input('Presione ENTER para continuar')
    
