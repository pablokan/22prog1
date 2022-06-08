# ingrese dos números enteros y luego los suma y muestra el resultado

validado = False
while not validado:
    n1 = input("Ingrese el primer entero: ")
    try:
        n1 = int(n1)
        validado = True
    except:
        print("No es un entero")

validado = False
while not validado:
    n2 = input("Ingrese el segundo entero: ")
    try:
        n2 = int(n2)
        validado = True
    except:
        print("No es un entero")

print("La suma es", n1 + n2)




