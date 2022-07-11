nombres = ["Juan", "Ana", "Pedro"]

# recorrido por índice
for i in range(len(nombres)):
    print(nombres[i])

# Si no hace falta el índice, RECORRER por ELEMENTO
for nombre in nombres: # para cada nombre en la lista nombres
    print(nombre)

posAna = nombres.index("Ana") # el find de las listas
print(posAna)

