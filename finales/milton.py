
# Modificar estas funciones para que
# resuelvan la ejecución de los ejemplos provistos.
# Se necesitan al menos dos funciones bien resueltas
# para aprobar el examen. 

# 1) Suma de una cantidad indeterminada de valores
def suma(*args):
    total = 0
    for n in args:
        total += n
    return total

print(suma(1, 2, 3)) # Devuelve: 6
print(suma()) # Devuelve: 0
print(suma(3, 4)) # Devuelve: 7


# 2) Cálculo de edad
import datetime
 
def edad(naci):
    hoy = datetime.date.today()
    if hoy < naci:
        print ("error en la fecha de nacimiento")
    else:
        ano = naci.year
        mes = naci.month
        dia = naci.day
 
        fecha = naci
        edad = 0
        while fecha < hoy:
            edad += 1
            fecha = datetime.date(ano+edad, mes, dia)
 
        return edad-1



edad(datetime.date(1965, 6, 3)) # Devuelve: 57 
edad(datetime.date(2000, 12, 3)) # Devuelve: 21
edad(datetime.date(1992, 11, 30)) # Devuelve: 29
edad(datetime.date(2007, 2, 29)) # Devuelve: 

"""# 3) Entrada de strings validada
# si no se cumple con el requisito tiene que volver a pedir lo mismo
def inputStr():
    usuario = inputStr("Nombre de usuario: ") 
    c = 0
    validusuario = False
    for i in len(usuario):
        c+=1
        if c > 4 and c < 6:
            validusuario = True
            print(usuario)
        while validusuario == False:
            usuario = input("Nombre de usuario")

    

inputStr()
"""