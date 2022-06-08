""" 
una función que se reutiliza
una función de único uso (carga?)
split? find? slicing?
"""
from input_choice import inputChoice

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

def cantXpais(pais):
    c = 0
    for p in personas:
        if pais in p:
            c += 1
    return f"La cantidad de personas de {pais} es {c}"

def fechasNacXletra(iA):
    for p in personas:
        posEsp = p.find(" ")
        if iA == p[posEsp+1]:
            print(p[-10:])

print(cantXpais("Argentina"))
paises = ["Germany", "United States", "Norway", "France"]
otroPais = inputChoice("Ingrese otro país además de Argentina: ", paises)
print(cantXpais(otroPais))

iA = input("Ingrese inicial de apellido: ") 
print(f'Las fechas de nacimiento de las personas cuyo apellido empieza con {iA} son:')
fechasNacXletra(iA)


