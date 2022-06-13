#Los apellidos de las personas nacidas antes de un año solicitado al usuario.
#En el punto 1) se puede optar en la función que se escriba, por retornar o bien imprimir
#  directamente los datos requeridos.

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
"""for i in range(len(personas)):
    apellido = personas[i]
    apellido.find("-2000")
print(apellido)  """
#La cantidad de personas nacidas en  Norway
#La cantidad de personas de un país ingresado por el usuario
def x():
    c = 0
    for i in range(len(personas)):
        if "Norway" in personas[i]:
            c += 1
    print("la cantidad de personas nacidas en Norway es", c)
x()
def i():
    cont = 0
    pais = input("ingrese un pais: ")
    for i in range(len(personas)):
        if pais in personas:
            cont += 1
    print(cont)
i()
