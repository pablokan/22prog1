# 1 Los apellidos de las personas nacidas antes de un año solicitado al usuario

personas = ["Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-04-2001",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-03-2002"]
nombres = []
paises = []
fecha = []
años = []
#aSolicitado = int(input("Ingrese año solicitado: "))
def nacimiento():
    for x in range(len(personas)):
        listas = (personas[x].split(","))
        nombres.append(listas[0])
        paises.append(listas[1])
        fecha.append(listas[2])
        
        
           
nacimiento()        

# La cantidad de personas nacidas en  Norway

paiselegido = "Norway"
def funcion(pais):
    contador = 0
    for x in range(len(personas)):
        if paiselegido in personas[x]:
            contador = contador + 1
    print("La cantidad de personas en Norway :", contador)
funcion(paiselegido)

paisBuscado = paisBuscado = input("Ingrese país buscado: ")
def funcion2():
    contador = 0
    for x in range(len(personas)):
        if paisBuscado in personas[x]:
            contador = contador + 1
    print("La cantidad de personas es :", contador)
funcion2()

"""paisesPosibles = ["France", "Argentina", "United States", "Norway", "Germany"]

respuesta = "Si"
funcion(paisBuscado)
while paisBuscado in paisesPosibles:
            cantidad = funcion(paisBuscado)
            print("La cantidad es: ", cantidad)
            break"""