def inputOpciones(msg, opciones):
    mensaje = f"{msg} ({opciones}): "
    listaOpciones = opciones.split("/")
    
    # mientras el país ingresado no esté en la lista de opciones, tiene que seguir dentro del while para seguir pidiendo el ingreso de un país correcto
    
    opcion = ""
    while opcion not in listaOpciones: 
        opcion = input(mensaje)

    return opcion

from input_number import inputNumber

def inputMenu(msg, opciones):
    print(msg)
    listaOpciones = opciones.split("/")
    for i in range(len(listaOpciones)):
        print(f"{i+1}) {listaOpciones[i]}")
    op = inputNumber(int, "Ingrese opción", 1, len(listaOpciones))
    return listaOpciones[op-1]


pais1 = inputOpciones("ingrese un país", "Albania/Sudán/Madagascar")
print(pais1)
pais2 = inputMenu("ingrese un país", "Albania/Sudán/Madagascar")
print(pais2)

color = inputMenu("ingrese un color", "rojo/verde/azul/amarillo")
print(color)

