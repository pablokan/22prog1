
def inputStr(mensaje, largo):
    s = ""
    while len(s) < largo: 
        s = input(mensaje)
    return s



t = inputStr("Ingrese una cadena de al menos 3 caracteres: ", 3)
w = inputStr("Ingrese una cadena de al menos 5 caracteres: ", 5)

print("Cadenas ingresadas: ", t, w)



