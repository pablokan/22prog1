# 1) Suma de una cantidad indeterminada de valores
print("<---------------------Suma--------------------->")
def suma(*args):
    total = sum(args)
    return total
print(suma(1,2,3))  #---> 6
print(suma())       #---> 0
print(suma(3,4))    #---> 7


print("<---------------------Cálculo de edad--------------------->")
# 2) Cálculo de edad

# print(edad('3/6/1965')) # Devuelve: 57
# print(edad('3/12/2000')) # Devuelve: 22
# print(edad('30/11/1992')) # Devuelve: 30
# print(edad('29/2/2007')) # Devuelve: 'Fecha inexistente'

def edad(fecha):
    from datetime import date
    day, month, year = fecha.split("/")

    day = int(day)
    month = int(month)
    year = int(year)
    
    hoy = date.today()
    
    try: 
        fecha = date(hoy.year, month, day) 
    except ValueError: 
        fecha = date(hoy.year, month, day-1) 
    if fecha > hoy:          
        print(hoy.year - year -1) 
    else: 
        print(hoy.year - year)
    
if __name__ == "__main__":
    fecha_nac = input("Ingrese su fecha de nacimiento Ej: 3/6/1965: ")

    edad(fecha_nac)


print("<------------------Entrada De Strings Validadas------------------->")
# 3) Entrada de strings validada

def inputStr(texto, min = 1, max = 100):

    aux = True
    while aux == True:
        dato = input(texto + ": ")
        if len(dato) <= max and len(dato) >= min:
            aux = False
            return dato
        else:
            print("el valor ingresado no es correcto segun el numero de caracteres")

usuario = inputStr("Nombre de usuario (entre 4 y 6 caracteres)", 4, 6)
texto = inputStr("Ingrese cualquier texto")
dni = inputStr("Número de documento", 8, 8)
password = inputStr("Ingrese una contraseña de 7 caracteres como mínimo", 7)
dominio = inputStr("Ingrese un sufijo de dominio web (ejemplo: com/ar/org/uk/edu/mil, de máximo 3 caracteres)", max=3)
