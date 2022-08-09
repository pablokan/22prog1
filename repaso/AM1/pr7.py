from json import loads
a = open("repaso/AM1/practico7.json")
s = a.read()
lista = loads(s)

listaLenguajes = []
for persona in lista:
    listaLenguajes += persona["languages"] # acumulo todas las listas en una sola

conjuntoLenguajes = set(listaLenguajes) # eliminar los repetidos al convertir en conjunto

# print(listaLenguajes, len(listaLenguajes))
# print(conjuntoLenguajes, len(conjuntoLenguajes))

listaLenguajesSinRepetir = list(conjuntoLenguajes) # vuelvo a convertir a lista para recorrer

listaResultados = []
mayor = 0
for lenguaje in listaLenguajesSinRepetir:
    # d = {lenguaje: listaLenguajes.count(lenguaje)}
    # listaResultados.append(d)
    contador = listaLenguajes.count(lenguaje)
    if  contador > mayor:
        mayor = contador
        lenguajeMasHablado = lenguaje

print(lenguajeMasHablado, mayor)


a.close()
