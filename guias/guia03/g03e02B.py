# Cargar letras en una lista (while). 
# Contar las vocales (for). 
# Mostrar el total.
letras = []
quiereSeguirCargando = "si"
while quiereSeguirCargando == "si":
    letra = input("Ingrese una letra: ")
    letras.append(letra)
    quiereSeguirCargando = input("Desea cargar mas letras?")

vocales = ["a", "e", "i", "o", "u"]
c = 0
for i in range(len(letras)):
    if letras[i] in vocales:
        c += 1 # c = c + 1
print("La cantidad de vocales es", c)

