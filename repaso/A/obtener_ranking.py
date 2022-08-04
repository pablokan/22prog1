a = open("repaso/A/ranking.txt")

filas = a.readlines()
print(filas)
lista = []
for fila in filas:
    usuario, intentos = fila.split(",")
    intentos = int(intentos[:-1])
    lista.append((intentos, usuario))

print(lista)
lista.sort()
print(lista)
a.close()
