# Hacer una función que dibuje una raya con un caracter y una longitud dada.

def raya(caracter, longitud):
    for i in range(longitud):
        print(caracter, end='')
    print()


raya("-", 10)
raya("+", 20)
raya("=",15)

