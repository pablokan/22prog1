# Dada una lista cargada con 
# 7 números enteros, obtener el promedio. 
# Mostrar por pantalla dicho promedio y 
# los números de la lista que sean 
# mayores que él.

total = 0
numeros = [10, 7, 8, 9, 4, 4, 12]
for i in range(7):
    total = total + numeros[i]
promedio = total / 7
print("El promedio es", promedio)
print("Y los números cargados mayores son")
for i in range(7):
    if numeros[i] > promedio:
        print(numeros[i])





