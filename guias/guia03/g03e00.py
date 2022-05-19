lista = ["a", "b", "a", "c", "d", "a", "e"]

borrar = input("Qué elemento desea borrar? ")
if borrar not in lista:
    print("no está")
else:
    while borrar in lista:
        lista.remove(borrar)

print(lista)
