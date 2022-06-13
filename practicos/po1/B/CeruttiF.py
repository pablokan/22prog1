# 1) Los apellidos de las personas nacidas antes de un año solicitado al usuario. 
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

def personasNacidas(añoSolicitado):
    añoSolicitado = int(input("Ingrese un año: "))
    for i in range(len(personas)):
        persona = personas[i]
        datos = persona.split(",")
        fechaNacimiento = datos[-1].split("-")
        añoNacimiento = int(fechaNacimiento[2])
        nombre = datos[0].split(" ")
        apellido = nombre[1]
        if añoNacimiento < int(añoSolicitado):
            print("los apellidos de las personas nacidas entes del", añoSolicitado,"son", apellido)
personasNacidas(añoSolicitado="2000")

# 2) La cantidad de personas nacidas en  Norway
def cantidadPersonas():
    c = 0
    for i in range(len(personas)):
        persona = personas[i]
        if "Norway" in persona:
            c+=1
    print("la cantidad de personas nacidas en Norway es", c)
cantidadPersonas()

# 3) La cantidad de personas de un país ingresado por el usuario.
paisIngresado = str(input("ingrese el nombre de un pais: "))
c = 0
for i in range(len(personas)):
    persona = personas[i]
    if paisIngresado in persona:
        c+=1
print("La cantidad de personas que hay en", paisIngresado, "es", c)


                                            # Francisco Cerutti, comision B.



