import sys

def inputInt(mensaje, min=-sys.maxsize, max=sys.maxsize):
    numero = 0
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = int(numero)
            if min <= numero <= max:
                validado = True
            else:
                if min != -sys.maxsize and max != sys.maxsize:
                    print('El rango de valores es entre', min, 'y', max)
                elif min != -sys.maxsize:
                    print('Debe ser mayor que', min-1)
                elif max != sys.maxsize:
                    print('Debe ser menor que', max+1)
                
        except:
            print("Error. Debe ingresar un número entero")
    return numero