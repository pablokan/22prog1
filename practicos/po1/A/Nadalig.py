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
    "Ambrosio Cadore,Norway,09-12-2002"]

nombres = []
paises = []
fechas = []
paisesAdmitidos = ['Germany', 'United States', 'Norway', 'France']
for x in personas:
    dividido = x.split(",")
    nombres.append(dividido[0])
    paises.append(dividido[1])
    fechas.append(dividido[2])

def validador(opciones):
    binotto = 0
    while binotto == 0:
        print(opciones)
        aValidar = str(input("Ingrese otro país además de Argentina: "))
        if aValidar in opciones:
            binotto = 1
            return(aValidar)
        else:
            print("Opcion Invalida")

def nacionalidades(lista, buscada):
    total = 0
    for x in lista:
        if buscada == x:
            total += 1
    print ("La cantidad de personas de", buscada, "es", total)
        
def buscadorFecha(listaNombres, listaFechas):
    letraBuscada = str(input("Ingrese inicial de apellido: "))
    letraBuscada = letraBuscada.upper()
    fechasEncontradas = []
    for x in range(len(listaNombres)):
        dividido = listaNombres[x].split(" ")
        apellido = dividido[1]
        if apellido[0] == letraBuscada:
            fechasEncontradas.append(listaFechas[x])
    print("Las fechas de nacimiento de las personas cuyo apellido empieza con", 
    letraBuscada, "son:")
    for x in fechasEncontradas:
        print(x)

nacionalidades(paises, "Argentina")
nacionalidades(paises, validador(paisesAdmitidos))
buscadorFecha(nombres, fechas)