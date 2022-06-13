personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(America),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-04-2001",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(Europe),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-03-2002"
]
# 1) Los apellidos de las personas nacidas antes de un año solicitado al usuario.
añoSolicitado = int(input("Ingrese un año: "))
def personasNacidas(añoIngresado):
    for x in range(len(personas)):
        persona = personas[x]
        datos = persona.split(",")
        fechaNacimiento = datos[-1].split("-")
        añoNacimiento = int(fechaNacimiento[2])
        nombreCompleto = datos[0].split(" ")
        apellido = nombreCompleto[1]
        if añoNacimiento < int(añoIngresado):
            print(apellido)
personasNacidas(añoSolicitado)

# 2) La cantidad de personas nacidas en  Norway
def personasNorway(): 
    c = 0
    for i in range(len(personas)):
        habitante = personas[i]
        if "Norway" in habitante:
            c += 1
    print("La cantidad de personas nacidad en Norway son: ", c)
personasNorway()


# 3) La cantidad de personas de un país ingresado por el usuario 
def cantidadPersonas(): 
    paisSolicitado = input("Ingrese un pais: ")
    c = 0
    for i in range(len(personas)):
        habitante = personas[i]
        if paisSolicitado in habitante:
            c += 1
    print("La cantidad de personas nacidad en", paisSolicitado, "son: ", c)
cantidadPersonas()