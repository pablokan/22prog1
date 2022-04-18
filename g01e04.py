# Leer dos números y decir cuál es el mayor.


n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

if n1 > n2:
    print("El mayor es", n1)
elif n1 == n2:
    print("los dos valen", n1)
else:
    print("El mayor es", n2)
