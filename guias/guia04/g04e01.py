frase = "River Plate vuelve a las copas."
nuevaFrase = ""

lista = frase.split("s")
for i in range(len(lista)):
    nuevaFrase += lista[i]

print(nuevaFrase)
