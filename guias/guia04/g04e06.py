frase = "Quiero comer manzanas, solamente manzanas, manzanas dije!"
palabra = "manzanas"

posi = 0
c = 0

# cambiando el punto de comienzo de la búsqueda
""" buscarDesde = 0
while posi != -1: # mientras exista la palabra
    posi = frase.find(palabra, buscarDesde)
    if posi != -1:
        c += 1
    buscarDesde = posi + 1
print(c)
"""

# cortando la frase para eliminar la palabra
while posi != -1:
    posi = frase.find(palabra)
    if posi != -1:
        c += 1
        frase = frase[posi+1:]
print(c)

