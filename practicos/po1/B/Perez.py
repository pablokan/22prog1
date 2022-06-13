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

pregunta = input("Ingrese el año que desea buscar: ")
pais = input("Ingrese un pais buscado: ")
nombre = ""
nacimiento = "Norway"
def funcAño():
    for x in range(len(personas)):
        if pregunta in personas[x]:
            nombre = personas[x].split(",")
            print(nombre[0])
funcAño()
"-----"
def cantPers():
    contador = 0
    contador2 = 0
    for x in range(len(personas)):
        if nacimiento in personas[x]:
            contador += 1
    print("La cantidad de personas de Norway es:",contador)
    for x in range(len(personas)):
        if pais in personas[x]:
            contador2 += 1
    print("La cantidad de personas nacidas en",pais,"es:",contador2,)
cantPers()