#Tengo un listado de personas, sus datos son:
#Nombre y Apellido - País de origen (Continente) - Fecha de nacimiento


personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-04-2001",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-03-2002"
]

#1. Los apellidos de las personas nacidas antes de un año solicitado al usuario.

AñoIngresado = 0
AñoNacimiento = 0

print("Ingrese el año de nacimiento: ")
AñoIngresado = int(input())
for x in range (len(personas)):
    persona = personas[x]
    persona = persona.split(",")
    añoNacimiento = persona[2]
    añoNacimiento = añoNacimiento.split("-")
    AñoNacimiento = int(añoNacimiento[2])
    if AñoNacimiento < AñoIngresado:
        print(persona[0])

#2. La cantidad de personas nacidas en  Norway #3.La cantidad de personas de un país ingresado por el usuario en una misma Funcion.

b = 0
c = 0
norway = 0
PaisIngresado = ""

print("Ingrese el pais de nacimiento dentro de las opcinones: Norway , Argentina , United States , France , Germany: ") 
PaisIngresado = input()
for x in range (len(personas)):
    if PaisIngresado == "Norway":
        b += 1
    print(" la cantidad de personas nacidas en Norway es:" , b )
    for x in range (len(personas)):
        persona = personas[x]
        persona = persona.split(",")
        paisOrigen = persona[1]
        paisOrigen = paisOrigen.split("(")
        paisOrigen = paisOrigen[1]
        c += 1
        while PaisIngresado != "Norway" and PaisIngresado != "United States" and PaisIngresado != "Argentina" and PaisIngresado != "Germany" and PaisIngresado != "France":
            print("Error , ingrese el pais de nacimiento dentro de las opciones: ")           
            PaisIngresado = input("")
            if PaisIngresado == "Argentina" or "United States" or "Germany" or "France":
                print("La cantidad de personas nacidas en ", PaisIngresado , "es: ", c)
                








        




