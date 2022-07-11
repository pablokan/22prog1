texto = "Quiero comer manzanas, solamente manzanas."

def cantidadLetras(t):
    c = 0
    for i in range(len(t)):
        if t[i] not in "., :;?!@#$%*()":
            c += 1
    return c

print("La cantidad de letras que tiene el texto es", cantidadLetras(texto))

k = 0
for i in range(len(texto)):
    if texto[i].isalpha and texto[i] not in " ,.":
        k += 1
print(k)
