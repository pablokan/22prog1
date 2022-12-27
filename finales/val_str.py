def inputStr(msg, min=1, max=1000):
    s = ""
    while not (min <= len(s) <= max): 
        s = input(f"{msg}: ")
    return s

usuario = inputStr("Nombre de usuario (entre 4 y 6 caracteres)", 4, 6)
texto = inputStr("Ingrese cualquier texto")
dni = inputStr("Número de documento", 8, 8)
password = inputStr("Ingrese una contraseña de 7 caracteres como mínimo", 7)
dominio = inputStr("Ingrese un sufijo de dominio web (ejemplo: com/ar/org/uk/edu/mil, de máximo 3 caracteres)", max=3)