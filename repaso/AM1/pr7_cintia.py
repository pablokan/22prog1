from json import loads
a = open("repaso/AM1/practico7.json")
s = a.read()
lista = loads(s)

listaLenguajes = []
for persona in lista:
    listaLenguajes += persona["languages"] # acumulo todas las listas en una sola

print(listaLenguajes)

listaResultados = []
mayor = 0
for lenguaje in listaLenguajes:
    contador = listaLenguajes.count(lenguaje)
    if  contador > mayor:
        mayor = contador
        lenguajeMasHablado = lenguaje

print(lenguajeMasHablado, mayor)


a.close()
