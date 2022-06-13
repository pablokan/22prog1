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

# Funcion 1
#----------------------------------------------------------------------------
def buscarEnArgentina(listaPersonas):
    c = 0
    for i in range(len(listaPersonas)):
        persona = listaPersonas[i]
        if "Argentina" in persona:
            c += 1
    return c

#----------------------------------------------------------------------------
print(buscarEnArgentina(personas))

#Funcion 2
#----------------------------------------------------------------------------

def buscar(listaDePersonas):
    c = 0 
    cartel = "Ingrese un país que quiera buscar en la lista: "
    País = validarPaís(cartel)
    for i in range(len(listaDePersonas)):
        Persona = listaDePersonas[i]
        if País in Persona:
            c += 1
    return c
print(buscar(personas, input("otro pais: "))

def validarPaís(cartel):
    paisesValidos = "Argentina, Germany, United States, Norway France"
    validado = False
    while not validado:
        país = input(cartel)
        try:
            x = paisesValidos.find(país)
            if x != -1:
                validado = True
        except:
            print("No es un país que este dentro de los elementos de la lista :")
    return país

#----------------------------------------------------------------------------

#Funcion 3
#----------------------------------------------------------------------------
fechaNacimientosPersonas = []

def fechaNacimientos():
    letra = input("Ingrese una letra:")
    for i in range(len(personas)):
        persona = personas[i]
        pos = persona.find(",")
        nuevaPersona = persona[:pos]
        pos = nuevaPersona.find(" ")
        nuevaPersona = nuevaPersona[pos+1:]
        if letra == nuevaPersona[0]:
            fechaNacimientosPersonas.append(nuevaPersona)
            persona = personas[i]
            nuevaPersona = persona.split(",")
            nuevaPersona = nuevaPersona[2]
            print(nuevaPersona)
            fechaNacimientosPersonas.append(nuevaPersona)
    return fechaNacimientosPersonas
#----------------------------------------------------------------------------


