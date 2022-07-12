infinite = 1e309  # actual python infinite

def inputChoice(listaOpc: list, mensaje: str='Elija una opción') -> str:
    mensaje = f'{mensaje} ({listaOpc}): '
    listaOpc = listaOpc.split('/')
    op = ''
    while op not in listaOpc:
        op = input(mensaje)
        if op not in listaOpc:
            print("No es una opción válida")
    return op

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

def inputStr(msg, min=0, max=infinite):
    valid = False
    while not valid:
        s = input(msg)
        if min <= len(s) <= max:
            valid = True
    return s

