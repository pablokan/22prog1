def inputInt(cartel): 
    validado = False
    while not validado:
        n = input(cartel)
        try:
            n = int(n)
            validado = True
        except:
            print("No ha ingresado un entero") 
    return n


n1 = inputInt("Ingrese el primer entero: ")
n2 = inputInt("Ingrese el segundo entero: ")
print(n1+n2)



