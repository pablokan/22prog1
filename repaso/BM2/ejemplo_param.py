infinite = 1e309
# Ejemplo con solamente parámetros nominados
def inputInt(mensaje="Ingrese un número", min=-infinite, max=infinite):
    sufijoMensaje = ''
    if min != -infinite and max != infinite:
        sufijoMensaje = f'(entre {min} y {max})'
    elif min != -infinite:
        sufijoMensaje = f'(mayor a {min-1})'
    elif max != infinite:
        sufijoMensaje = f'(menor a {max+1})'
    mensaje = f'{mensaje} {sufijoMensaje}: '
    numero = ''
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = int(numero)
            if min <= numero <= max:
                validado = True
            else:
                print('valor fuera de rango')
                
        except:
            print(f"Error. Debe ingresar un número entero")
    return numero

if __name__ == '__main__':
    
    m = inputInt() # puedo no enviar ningún argumento porque todos los parámetros tienen su valor por defecto
    print(f"{m=}")
    
    i = inputInt('Ingrese una edad', 13, 17) # no se requiere enviar el nombre del parámetro
    print(f"{i=}")
    
    maxito = inputInt('ingrese un entero bajo', max=999) # especifico max para que distinga
    print(f"{maxito=}")
    
    minito = inputInt('ingrese un real alto', 1001) # si respeto el orden da igual que le ponga el min=
    print(f"{minito=}")

