def inputInt(cartel):
    validado = False
    while not validado:
        n = input(cartel)
        try:
            n = int(n)
            validado = True
        except:
            print("No es un entero")
    return n

numero1 = inputInt("Ingrese el primer entero: ")
numero2 = inputInt("Ingrese el segundo entero: ")
print("La suma es", numero1 + numero2)



