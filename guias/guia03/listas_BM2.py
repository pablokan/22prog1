""" a = [2, "hola", -8.1, "chau", 88]  # lista

print(a[1])  # a sub 1
print(a)
print("Cantidad de elementos de a: ", len(a))

print("Recorrido por índice")
for i in range(len(a)):
    print(a[i])

print("Recorrido por elemento")
for elemento in a:
    print(elemento)


b = []  # lista vacía
# b[0] = 11 esto da error porque no existe la posición cero aún
b = ["q"]
print(b)
b[0] = 11
print(b)


c = []
print(c)
c.append("primero")
print(c)
c.append("segundo")
print(c)
c.insert(1, "AL MEDIO")
print(c)
c[1] = "reemplazo al del medio"
print(c)
c.insert(0, "principio")
print(c)
c.pop(1)  # borra por posición, sin argumento borra el último
print(c)
c.remove("segundo") # borra por valor
print(c)
"""

""" 
listaNombres = []
for i in range(5):
    nombre = input("Nombre: ")
    listaNombres.append(nombre)

print(listaNombres)
"""

# Listas paralelas
nombres = ["Juan", "Ana", "Luis"]
edades = [32, 87, 12]

for i in range(len(nombres)):
    print(nombres[i], edades[i])
