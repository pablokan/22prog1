# Cuántas veces se repite una letra cualquiera. Parámetros: letra, cadena.

def contarLetra(letra, cadena):
    c = 0
    for x in range(len(cadena)):
        if cadena[x] == letra:
            c += 1
    return c

cantidad = contarLetra("o", "Hola como te va")
print("<Hola como te va> tiene", cantidad, "de veces la letra <o>")

l = "a"
s = "A la gilada ni cabida"

cantidad = contarLetra(l, s)
print("La cadena", s, "tiene", cantidad, "veces la letra", l)



