validado = False
while not validado:
    n1 = input("Ingrese el primer entero: ")
    try:
        n1 = int(n1)
        validado = True
    except:
        print("No ha ingresado un entero")

validado = False
while not validado:
    n2 = input("Ingrese el segundo entero: ")
    try:
        n2 = int(n2)
        validado = True
    except:
        print("No ha ingresado un entero")

print(n1+n2)
