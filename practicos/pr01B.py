from input_choice import inputChoice

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


def cantXpais(pais):
    c = 0
    for persona in personas:
        if pais in persona:
            c += 1
    return f"La cantidad de personas de {pais} es {c}"

def nacidosAntesDel(a):
    for p in personas:
        if int(p[-4:]) < a:
            posEsp = p.find(" ")
            posComa = p.find(",")
            apellido = p[posEsp+1:posComa]
            print(apellido)

antes = int(input("Ingrese año: "))
print(f'Los apellidos de las personas nacidas antes del {antes} son:')
nacidosAntesDel(antes)
print()
print(cantXpais("Norway"))
paises = ["Germany", "Norway", "United States", "Argentina", "France"]
otroPais = inputChoice("Ingrese uno de los países aceptados: ", paises)
print(cantXpais(otroPais))



