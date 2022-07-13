# Tipos de funciones:
# 1) Subprogramas
# 2) Funciones propiamente dichas

# 1
""" nombres = []
def carga():
    respuesta = "si"
    while respuesta == "si":
        nombre = input("Ingrese un nombre: ")
        nombres.append(nombre)
        respuesta = input("Quiere repetir? ")

def proceso():
    for nombre in nombres:
        print("Nombre: ", nombre)

carga()
proceso()
"""
# 2

def inputStr(mensaje, min, max):
    valid = False
    while not valid:
        s = input(mensaje)
        if min <= len(s) <= max:
            valid = True
        else:
            print("Longitud de la cadena fuera de rango")
    return s

salida = inputStr("Ingrese una cadena entre 3 y 5: ", 3, 5)
print(f"{salida=}")

otraSalida = inputStr("Ingrese una cadena entre 1 y 3: ", 1, 3)
print(f"{otraSalida=}")







