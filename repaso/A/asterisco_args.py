def suma(*args):
    s = 0
    for numero in args:
        s += numero
    return s

print(suma(1,2,3))
print(suma(1,3,5,5,5))
print(suma())


def sumaLista(lista):
    s = 0
    for numero in lista:
        s += numero
    return s

numeros = []
hayaDatos = "si"
while hayaDatos == "si":
    n = int(input("Ingrese numerito: "))
    numeros.append(n)
    hayaDatos = input("Hay mas? ")

print(sumaLista(numeros))
