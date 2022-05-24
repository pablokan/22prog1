# Cuántas veces se repite una letra cualquiera. Parámetros: letra, cadena.

def letraRepetida(letra, cadena):
    c = 0
    for i in range(len(cadena)):
        if cadena[i] == letra:
            c += 1
    return c

print(letraRepetida("o", "hola como te va"))

k = input("Ingrese una cadena: ")
l = input("Ingrese una letra para buscar: ")
print(letraRepetida(l, k))



#print("La letra", letra, "está", c, "veces en la cadena", cadena)



