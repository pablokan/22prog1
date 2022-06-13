personas = [
    "Vikki Tewkesbury,France,30-01-2000",
    "Virgie Brach,France,04-02-1994",
    "Adeline La Padula,France,18-06-2002",
    "Willy Branscombe,Argentina,21-11-1997",
    "Diane Piffe,France,07-08-1993",
    "Britta Causbey,France,24-04-1991",
    "Elisabeth Cleeve,France,04-03-1991",
    "Rafael Ivanchenkov,France,28-04-2002",
    "Zerk Milsom,Norway,03-12-1994",
    "Adorne Ovington,United States,17-08-1991",
    "Kathryn Backshell,United States,04-03-1992",
    "Blake Colbeck,United States,18-01-1999",
    "Arron Bresnahan,United States,03-07-2001",
    "Deloria Dominguez,France,31-07-1990",
    "Grenville Aldersea,Argentina,11-01-2001",
    "Jemimah Haughian,Argentina,30-11-1998",
    "Con Gethen,United States,06-06-1992",
    "Roxie Igoe,France,31-03-2002",
    "Hollyanne Mottley,United States,05-01-1996",
    "Ambrosio Cadore,Norway,09-12-2002"
]

#La cantidad de personas de Argentina
contador=0
for i in range (len(personas)):
    persona = personas[i]
    print(persona)
    if "Argentina" in persona:
        persona = persona.split (",")
        print(persona [2])
        lugar = persona [2]
        contador += 1
print("la cantidad de persona en Argentina son:", contador)

""" 
#La cantidad de personas de un país ingresado por el usuario
contador=0
for i in range (len(personas)):
    lugar = input("ingrese un pais:")
    persona = personas[i]
    persona = persona.split(",")
    if lugar == 'Germany' 'United States' 'Norway' 'France' in persona:
     contado = contador + 1
    else:
        lugar != 'Germany' 'United States' 'Norway' 'France'
print("La cantidad de personas en:", lugar, "son:", contador)
 """

#Las fechas de nacimiento de las personas cuyo apellido comience con una letra solicitada al usuario
for i in range (len(personas)):
    letra = input("ingrese una letra:")
    persona = personas[i]
    if letra in persona:
        persona = persona.split("/")
        print(persona [3])
        fecha = (persona [3])
print("La fecha es:",fecha )


        
