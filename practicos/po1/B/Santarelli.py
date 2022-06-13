"""
Quiero obtener:
Los apellidos de las personas nacidas antes de un año solicitado al usuario.
La cantidad de personas nacidas en  Norway
La cantidad de personas de un país ingresado por el usuario 

En el punto 1) se puede optar en la función que se escriba, por retornar o bien imprimir directamente los datos requeridos.

Para los puntos 2) y 3) se requiere usar la misma función

Adicionalmente, para el punto 3) se debe restringir el país aceptado en el ingreso a los 5 que existen en el listado: Germany, Norway, United States, Argentina y France. 
"""
from operator import truediv
from re import A


personas = ["Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(America),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-04-2001",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(Europe),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-03-2002"]
def nacimientos(añosolicitado):
    print("Los apellidos nacidos antes del",añosolicitado,"Son: ")
    for x in range (len(personas)):
        persona=personas[x]
        datos=persona.split(",")
        nacimiento=datos[2].split("-")
        añodenacimiento=nacimiento[2]
        nombreentero=datos[0].split(" ")
        apellido=nombreentero[1]
        if int(añosolicitado) > int(añodenacimiento):
            print(apellido)

def cantdepersonas(territorio):
    contador=0
    for x in range(len(personas)):
        persona=personas[x]
        datos=persona.split(",")
        lugar=datos[1]
        posicióndelparentesis=lugar.find("(")
        pais=lugar[:posicióndelparentesis]
        if pais == territorio:
            contador+=1
    return contador
print("Opciones: 'Germany', 'Norway', 'United States', 'Argentina', 'France'")

def validacion(lista):
    validado=False
    opcion=input("Ingrese uno de los países aceptados: ")
    while not validado:
        if opcion in lista:
            validado=True
        else:
            print("Opción inválida")
            opcion=input("Ingrese uno de los países aceptados: ")
    return opcion



if __name__ == "__main__":
    #ejercicio 1:
    añosolicitado=input("Ingrese año: ")
    nacimientos(añosolicitado)
    #ejercicio 2:
    territorio=input("Ingrese uno de los países aceptados: ")
    cantdepersonas(territorio)
    #ejercicio 3:
    
    lista=['Germany', 'Norway', 'United States', 'Argentina', 'France']
    validacion(lista)