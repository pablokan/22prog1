from input_pais import inputPais
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

listaPaises = ['GERMANY', 'NORWAY', 'UNITED STATES', 'ARGENTINA', 'FRANCE']

def apellidosAnterioresA(anio):
    for persona in personas:
        aN = int(persona[-4:])
        if aN < anio:
            posEsp = persona.find(" ")
            posComa = persona.find(",")
            apellido = persona[posEsp+1:posComa]
            print(apellido)

def personasXpais(pais):
    c = 0
    for persona in personas: # for i in range(len(personas))
        if pais.upper() in persona.upper(): # if pais in personas[i]
            c += 1
    return f"La cantidad de personas de {pais} es {c}"


# Punto 1
a = int(input("Ingrese año: "))
print(f"Los apellidos de las personas nacidas antes del año {a} son: ")
apellidosAnterioresA(a)

# Punto 2
print(personasXpais("Norway"))

# Punto 3
unPais = inputPais("Ingrese un país permitido: ", listaPaises)
print(personasXpais(unPais))



