# Pedir dos números enteros y sumarlos

numero1 = input("Ingrese un número entero: ")  # ingresa el dato como string
numero1 = int(numero1)  # convierte el dato en entero (int)

# combino el input con el int en una sola línea
numero2 = int(input("Ingrese otro número entero: "))

# print(numero1 + numero2) # hacer la suma dentro del print
suma = numero1 + numero2
print("La suma es", suma)
