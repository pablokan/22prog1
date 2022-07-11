# Preguntar si hay datos para ingresar, en caso afirmativo
# solicitar un número entero y decir si es negativo o no.
# Preguntar si repite.

respuesta = input("Hay datos para ingresar? ")
while respuesta == "si":
    n = int(input("Ingresar un entero: "))
    if n < 0:
        print("es negativo")
    else:
        print("NO es negativo")
    respuesta = input("Quiere repetir? ")
