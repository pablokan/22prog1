# Dada una lista con números, 
# crear otra con los cuadrados de esos valores. 

numeros = [2, 3, 4]
cuadrados = []

for x in range(len(numeros)):
    cu = numeros[x] * numeros[x]
    cuadrados.append(cu)

print(numeros, cuadrados)