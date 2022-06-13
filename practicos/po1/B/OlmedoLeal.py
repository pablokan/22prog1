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

# 1) Los apellidos de las personas nacidas antes de un año solicitado al usuario.

años = ["2000", "1994", "2002", "2007", "1993", "2001", "1991"]
def contadorPersonas(personas):
    contador = 0
    for i in range(len(personas)):
        if años == personas[i]:
            contador = contador + 1
    print(contador)

user = input("Ingrese un año solicitado: ")
contadorPersonas(user)



print("==================")
print("==================")
print("==================")

# 2) La cantidad de personas nacidas en  Norway

def cantPersonas(paises):
    contador = 0
    for x in range(len(personas)):
        cant = personas[x]
        cant == cant.split(",")
        if cant[1] == paises:
            contador = contador + 1
    return contador

print(cantPersonas("Norway"), "son las personas que viven en Norway")



# 3)

"""
paises = input("Ingrese un pais: ")
obligado = ["Argentina", "United States", "Norway", "France", "Germany" ]
contador = 0
"""


