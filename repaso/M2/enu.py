nombres = ["Juan", "Ana", "Luisa", "Pepe"]
sexos = ["m", "f", "f", "m"]

for i, nombre in enumerate(nombres):
    if sexos[i] == "f": # recorre por índice
        print(nombre) # recorre por elemento
print("------------------------------")
for n, nombre in enumerate(nombres, 10):
    print(n, nombre)
