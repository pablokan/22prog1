a = open("repaso/BM2/ranking.miles", "r", encoding="utf-8")
lista = a.readlines()
print(lista)
listaJ = []
for jugador in lista:
    nombre, intentos = jugador.split(",")
    intentos = int(intentos[:-1])
    listaJ.append([intentos, nombre])

print(listaJ)
listaJ.sort()
print("Ranking")
for j in listaJ:
    fila = f"Jugador: {j[1]}. Intentos: {j[0]}"
    print(fila)
a.close()
