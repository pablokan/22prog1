cadena = "Quiero comer manzanas, solamente manzanas, dije manzanas."
laQueQuieroCambiar = "manzanas"
laQueQuieroPoner = "peras"

def reemplazarPalabra(palabraNueva, palabraVieja, frase):
    while palabraVieja in frase:
        posPalVieja = frase.find(palabraVieja)
        if posPalVieja != -1:
            inicio = frase[:posPalVieja]
            final = frase[posPalVieja+len(palabraVieja):]
            frase = inicio + palabraNueva + final
    return frase

nuevaCadena = reemplazarPalabra(laQueQuieroPoner, laQueQuieroCambiar, cadena)
print(nuevaCadena)
otraNuevaCadena = reemplazarPalabra("río", "mar", "El próximo verano iremos al mar, de ser posible al mar Caribe")
print(otraNuevaCadena)
df



