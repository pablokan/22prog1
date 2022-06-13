personas = [
    "Vikki Tewkesbury,France,30-01-2000",
    "Virgie Brach,France,04-02-1994",
    "Adeline LaPadula,France,18-06-2002",
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

#Listas para trabajar mejor los datos.
nombres=[]
paises=[]
fechas=[]

#Descomponer solo serapa en 3 listas paralelas de datos para poder trabajarlos mejor.
def descomponer(personas,nombres,paises,fechas):
    for i in range(len(personas)):
        datos=personas[i].split(",")
        nombre=datos[0]
        pais=datos[1]
        fecha=datos[2]
        nombres.append(nombre)
        paises.append(pais)
        fechas.append(fecha)

descomponer(personas,nombres,paises,fechas)

#1)La cantidad de personas de Argentina

def cantidadPersonas(paises,paisBuscado):
    cant=0
    for i in range(len(paises)):
        if paisBuscado=="Argentina":
            if paises[i]==paisBuscado:
                cant+=1
        if paisBuscado!="Argentina":
            if paises[i]==paisBuscado:
                cant+=1
    return(cant)

#La cantidad de personas de un país ingresado por el usuario.
""" ValidarPais verifica que paisBuscado sea ingresado correctamente.
    Ademas validarPais ejecuta cantidadPersonas para contar la cantidad de personas del pais ingresado
"""

def validarPais(paises):
    validado=True
    while validado==True:
        print("Opciones: ['Germany', 'United States', 'Norway', 'France']")
        paisBuscado=input("Ingrese otro país además de Argentina: ")
        try:
            if paisBuscado in ('Germany', 'United States', 'Norway', 'France'):
                validado=False
                return(cantidadPersonas(paises,paisBuscado))
        except:
            print("Opcion Invalidad")
     

#Las fechas de nacimiento de las personas cuyo apellido comience con una letra solicitada al usuario.

def fechasNacimientos(nombres,fechas):
    inicial=input("Ingrese inicial de apellido: ")
    print("Las fechas de nacimiento de las personas cuyo apellido empieza con",inicial,"son: ")
    for i in range(len(nombres)):
        apellido=nombres[i].find(" ")
        if inicial in nombres[i][apellido:apellido+2]:
            return(fechas[i])


""" Main"""
personasArgentina=cantidadPersonas(paises,"Argentina")
print("La cantidad de personas de Argentina es",personasArgentina)
print("")
personasOtroPais=validarPais(paises)
print("La cantidad de personas de otro pais es",personasOtroPais)
print("")
fechasInicial=fechasNacimientos(nombres,fechas)
print(fechasInicial)