validado = False
while not validado:
    try:
        n1 = input("Ingrese el primer entero: ")
        n1 = int(n1)
        validado = True
        n2 = input("Ingrese el segundo entero: ")
        n2 = int(n2)
        validado = True
    except:
        print("No ha ingresado un entero")

print(n1+n2)
