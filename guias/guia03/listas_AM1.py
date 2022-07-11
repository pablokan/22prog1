"""
a = [9, "jota", -8.2, "riquelme", 222]

print(a[1])  # muestra el segundo elemento porque el primero está en posición cero

print(a)  # muestra toda la lista con los corchetes

print("Cantidad de elementos de la lista a: ", len(a))  # len: longitud

print("Recorrido por índice")
for indice in range(len(a)):  # indice se mueve por posición
    print(a[indice])

print("Recorrido por elemento")  # elemento se mueve por los valores
for elemento in a:
    print(elemento)


b = []  # lista vacía
# b[0] = 111  # IndexError: list assignment index out of range
# No funcionó porque la posición cero aún no existe

b = ["q"]
print(b)
b[0] = 111  # esto ahora si funciona porque la pos. cero ya tenía valor
print(b)


c = []
c.append("primero")
print(c)
c.append("segundo")
print(c)
c.insert(1, "al medio")
print(c)
c[1] = "reemplazo al que estaba al medio"
print(c)
c.pop(1)  # elimina por posición, por defecto el último
print(c)
c.remove("primero")  # elimina por valor
print(c)


listaNombres = []
for i in range(5):
    nombre = input("Ingrese un nombre: ")
    listaNombres.append(nombre)

print(listaNombres)
"""

# Listas pararelas
nombres = ["Juan", "Ana", "Luis"]  # misma posición, misma persona
edades = [32, 87, 12]  # entonces Juan tiene 32 años

personas = [["Juan", 32], ["Ana", 87], ["Luis", 12]]  # es lo mismo con listas anidadas
