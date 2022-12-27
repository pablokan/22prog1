
# Modificar estas funciones para que
# resuelvan la ejecución de los ejemplos provistos.
# Se necesitan al menos dos funciones bien resueltas
# para aprobar el examen. 

# 1) Suma de una cantidad indeterminada de valores
# 2) Cálculo de edad
def edad(fecha):
    from datetime import date
    # usar date para validar fecha de entrada
    # Por ejemplo: date(2001, 2, 29) da error   
    hoy = date.today()

    d,m,a =fecha.split("/")
    edad=0
    dia= int(d)
    mes=int(m)
    año=int(a)

    if dia < hoy.day and mes <hoy.month:
        edad= hoy.year -año
        if  dia>hoy.day and mes > hoy.month:
            edad= hoy.year - año + 1
            if dia== hoy.day and mes== hoy.month:
                edad=  hoy.year - año +1
                if dia> 28 and mes == 2:

                    edad="fecha incorrecta"
            

    return edad


print(edad('3/6/1965')) # Devuelve: 57
print(edad('3/12/2000')) # Devuelve: 21
print(edad('30/11/1992')) # Devuelve: 29
print(edad('29/2/2007')) # Devuelve: 'Fecha inexistente'

# 3) Entrada de strings validada
# si no se cumple con el requisito tiene que volver a pedir lo mismo


def inputStr(str,min=1,max=999):
    prueba= True

    while prueba == True:
        cadena=input(str)
        cC=0
        for x in range( len(cadena)) :
            cC+=1
        if cC>=min and cC<=max:
                prueba=False

        else:
                        print("cantidad de caracteres incorrectos")

             
             
        
        



usuario = inputStr("Nombre de usuario (entre 4 y 6 caracteres)", 4, 6)
texto = inputStr("Ingrese cualquier texto")
dni = inputStr("Número de documento", 8, 8)
password = inputStr("Ingrese una contraseña de 7 caracteres como mínimo", 7)
dominio = inputStr("Ingrese un sufijo de dominio web (ejemplo: com/ar/org/uk/edu/mil, de máximo 3 caracteres)", max=3)

