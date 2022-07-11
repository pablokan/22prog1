#  Pedir el ingreso de 5 números. 
# Contar los mayores de 23 y almacenar 
# los que cumplen la condición.  
# Mostrar la cantidad y los números 
# guardados.
may23 = []
print("Pedido de 5 números")
for i in range(5):
    numero = int(input("Ingrese número: "))
    if numero > 23:
        may23.append(numero)

print("Los números que cumplen con la condición de ser mayores a 23 son", may23, "y la cantidad de ellos es", len(may23))

