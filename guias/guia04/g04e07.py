frase = "Quiero comer manzanas, solamente manzanas, dije manzanas."

palabraVieja = "manzanas"
palabraNueva = "peras"

while palabraVieja in frase:
    posPalVieja = frase.find(palabraVieja)
    if posPalVieja != -1:
        inicio = frase[:posPalVieja]
        final = frase[posPalVieja+len(palabraVieja):]
        frase = inicio + palabraNueva + final
       
print(frase)





