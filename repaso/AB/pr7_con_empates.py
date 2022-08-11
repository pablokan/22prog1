from json import loads
from collections import Counter

a = open("repaso/AB/practico7.json", "r", encoding="utf-8")
s = a.read()
personas = loads(s)

todosLosLenguajes = []
for persona in personas:
    todosLosLenguajes += persona["languages"]

mayor = 0
lista = []
masHablados = []
for lenguaje in todosLosLenguajes:
    cantidad = todosLosLenguajes.count(lenguaje)
    lista.append([lenguaje, cantidad])
    if cantidad > mayor:
        mayor = cantidad

for l in lista:
    if l[1] == mayor:
        masHablados.append(l[0])

print("Lenguaje(s) más hablado(s):")
print("Cantidad:", mayor)
for l in list(set(masHablados)): # el set es para limpiar las repeticiones
    print(l)
    


