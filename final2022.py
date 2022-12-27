
# Modificar estas funciones para que
# resuelvan la ejecución de los ejemplos provistos.
# Se necesitan al menos dos funciones bien resueltas
# para aprobar el examen. 

# 1) Suma de una cantidad indeterminada de valores
def suma(*args):
    return sum(args)
    

print(suma(1, 2, 3)) # Devuelve: 6
print(suma()) # Devuelve: 0
print(suma(3, 4)) # Devuelve: 7
""" 
# 2) Cálculo de edad
def edad():
    from datetime import date
    # usar date para validar fecha de entrada
    # Por ejemplo: date(2001, 2, 29) da error   
    hoy = date.today()
    return hoy.day, hoy.month, hoy.year

print(edad('3/6/1965')) # Devuelve: 57
print(edad('3/12/2000')) # Devuelve: 21
print(edad('30/11/1992')) # Devuelve: 29
print(edad('29/2/2007')) # Devuelve: 'Fecha inexistente'

 """
# 3) Entrada de strings validada
# si no se cumple con el requisito tiene que volver a pedir lo mismo
def inputStr(msg, min=1, max=100000000000):
    s = ''
    while not (min <= len(s) <= max):
        s = input(msg)
    return s 

usuario = inputStr("Nombre de usuario (entre 4 y 6 caracteres)", 4, 6)
texto = inputStr("Ingrese cualquier texto")
dni = inputStr("Número de documento", 8, 8)
password = inputStr("Ingrese una contraseña de 7 caracteres como mínimo", 7)
dominio = inputStr("Ingrese un sufijo de dominio web (ejemplo: com/ar/org/uk/edu/mil, de máximo 3 caracteres)", max=3)

