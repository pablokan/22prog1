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
DivisionDeDatos=[]
Nombres=[]
Apellidos=[]
fechas=[]
pais=[]
fechasDesglosadas=[]
años=[]
añosUsuario=int(input("Ingrese año: "))
contador=0
for x in range(len(personas)):
    DivisionDeDatos.append(personas[x].split(","))
for x in range(len(DivisionDeDatos)):
    fechas.append(DivisionDeDatos[x][2])
    Nombres.append(DivisionDeDatos[x][0])
for x in range(len(fechas)):
    fechasDesglosadas.append(fechas[x].split("-")) 
for x in range (len(fechasDesglosadas)):
    años.append(fechasDesglosadas[x][2])
print("1) Estos son los apellidos de las personas nacidas antes del año",añosUsuario)    
for x in range(len(años)):
    if int(años[x])< añosUsuario:
        posicionEspacio=Nombres[x].find(" ")
        print(Nombres[x][posicionEspacio:])

def cantidadPorPais():
    contador=0
    paisBuscado=input("Ingrese pais buscado: ")
    for x in range(len(DivisionDeDatos)):
        pais.append(DivisionDeDatos[x][1])
        posicionParentesis=pais[x].find("(")
        if (pais[x][:posicionParentesis])==paisBuscado:
            contador+=1
    return(paisBuscado, contador)
a,b=(cantidadPorPais())
print("2) La cantidad de personas nacidas en",a,"son",b) #no pude hacer la validacion.      