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


def buscarAño(year):
    lista_apellidos=[]
    fechas = []
    nombres = []
    for x in range(len(personas)):
        split = personas[x].split(",")
        nombres.append(split[0])
        fechas.append(split[2])
        fechaSplit = fechas[x].split("-")
        nombresSplit = nombres[x].split(" ")
        if year > int(fechaSplit[2]):
            lista_apellidos.append(nombresSplit[1])
    print("Los apellidos de las personas nacidas antes del", year ,"son:",lista_apellidos)
buscarAño(int(input("Ingrese año: ")))

def buscarPais():
    list_paises = []
    contador = 0
    validado =False
    while not validado:
        pais = input("Ingrese uno de los países aceptados: ")
        for x in range(len(personas)):
            split = personas[x].split(",")
            list_paises.append(split[1])
            splitPaies = list_paises[x].split("(")
            if splitPaies[0] == pais:
                contador +=1 
                validado = True
        if contador == 0:
            print("Opción inválida")
        else:
            print("La cantidad de personas de",pais,"es:",contador)

def buscarNorway(pais= ""):
    if pais != "":
        contador = 0
        paises = []
        for x in range(len(personas)):
            split = personas[x].split(",")
            paises.append(split[1])
            splitPaies = paises[x].split("(")
            if splitPaies[0] == pais :
                contador +=1 
        print("La cantidad de personas de",pais,"es: ", contador)
    else:
        buscarPais()

# 2 Opciones de busqueda ->
buscarNorway("Norway")
buscarNorway()
  



