from io import open

listaPrimos = []
listaFelices = []
listaComunes = []

archivo1 = open("Tercero/numerosprimos.txt","r")
archivo2 = open("Tercero/numerosfelices.txt","r")

for x in archivo1:
    listaPrimos.append(int(x))

for x in archivo2:
    listaFelices.append(int(x))

archivo1.close()
archivo2.close()


for valor in listaPrimos:
    if valor in listaFelices:
        listaComunes.append(valor)

print(listaPrimos)
print('')
print(listaFelices)
print('')
print(listaComunes)

fichero = open("Tercero/numeroscomunes.txt","a")

for valor in listaComunes:
    fichero.write(str(valor)+"\n")

fichero.close()