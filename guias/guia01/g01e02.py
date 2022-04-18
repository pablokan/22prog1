# Pedir tres notas, calcular el promedio y mostrarlo.

nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))
nota3 = float(input("Ingrese nota 3: "))

suma = nota1 + nota2 + nota3
promedio = suma / 3
print("El promedio es", promedio)


# lo mismo en una sola línea
# print("El promedio es", (nota1 + nota2 + nota3) / 3)
