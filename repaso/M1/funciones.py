# Funciones:
# 1) Sub programas
# 2) Funciones propiamente dichas

# def Sub programa de Carga que se ejecuta una sola vez
def carga():
    while True:
        # proceso de carga
        pass

# Función en sentido estricto
def inputStr(mensaje, min=0, max=1000):
    valid = False
    while not valid:
        i = input(mensaje)
        if min <= len(i) <= max:
            valid = True
    return i

s1 = inputStr("Ingrese una cadena de al menos 3 caracteres: ", 3)
print("Cadena ingresada: ", s1)

s2 = inputStr("Otra cadena de minimo 5: ", 5)
print("Cadena ingresada: ", s2)

