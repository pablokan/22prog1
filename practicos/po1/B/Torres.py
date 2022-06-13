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

# Los apellidos de las personas nacidas antes de un año solicitado al usuario.

def funcion():
    nacimiento= input("ingrese año de nacimiento y le mostrara el apellido de las personas nacidas antes del año que ingreso: ")
    for x in range(len(personas)):
        gente = personas[x]
        gente = gente.split(",")
        año = gente[2]
        año = año[6:]
        if nacimiento > año:
            gente = gente[0]
            gente = gente.split(" ")[1]
            print(gente)


#La cantidad de personas nacidas en  Norway

def cantidad():
    c = 0
    for x in range(len(personas)):
        if "Norway" in personas[x]:
            c = c + 1
    print("la cantidad de personas que nacienron en Norway son: ", c)

cantidad()

def validacion(cartel):
    validado = False
    while not validado:
        n = input(cartel)
        if  n == "Germany" or  n == "Norway" or n == "United States" or  n == "Argentina" or n == "France":
            print("el pais que eligio es valido")
        else:
            print("opcion invalida")
    return n
validar = validacion("ingrese un pais: ")
print(validar)






