infinite = 1e309 # 10 elevado a la potencia 309

def inputNumber(dataType, mensaje="Ingrese un número", min=-infinite, max=infinite):
    sufijoMensaje = ''
    tipoNum = {int: 'entero', float: 'real'}
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
            numero = dataType(numero)
            if min <= numero <= max:
                validado = True
            else:
                print('valor fuera de rango')
                
        except:
            print(f"Error. Debe ingresar un número {tipoNum[dataType]}")
    return numero

if __name__ == '__main__':
    q = inputNumber(int)
    edad = inputNumber(int, "ingrese su edad")
    w = inputNumber(int, "sueldo", 10_000, 100_000)