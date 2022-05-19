# Ingresar nombres en una lista, luego buscar un nombre y
# de encontrarlo decir en qué posición está.

lista = ["Pedro", "Ana", "Luisa", "José"]
nombreBuscado = "Luisa"

for i in range(len(lista)):
    if nombreBuscado == lista[i]:
        break  # rompe el for para no seguir dando vueltas sin necesidad
print("Encontrado en la posición", i)

print(lista.index("Luisa"))  # trampa directa
