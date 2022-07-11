# Mostrar por pantalla una lista de 10 números enteros consecutivos,
# comenzando con un número ingresado por teclado.

valorInicial = int(input("Ingrese un valor inicial: "))
print("Los diez enteros consecutivos son:")
for x in range(valorInicial, valorInicial + 10):
    print(x)
