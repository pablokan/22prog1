# Solicitar 3 edades y obtener el promedio

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


t = 0
for x in range(3):
    e = inputInt("Ingrese edad: ")
    t += e
print("El promedio de edades es", t//3)

