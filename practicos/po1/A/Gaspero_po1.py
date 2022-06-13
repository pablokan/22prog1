#La cantidad de personas de Argentina
#La cantidad de personas de un país ingresado por el usuario 
#Las fechas de nacimiento de las personas cuyo apellido comience 
# con una letra solicitada al usuario

def cuentaCantidad (lista,datoAContar):
    contador = 0
    for i in lista:
        if i == datoAContar:
            contador += 1
    return contador
def listaCadena (lista):
    cadena = " "
    for i in lista:
        cadena += i + ","
    return cadena

def valid (lista):
    c = -1
    while c < 0:
        busPais2 = input("De que otro pais desea saver la cantidad: ")
        b = (listaCadena (lista)).find(busPais2)
        c = b
        if c == -1:
            print("Ese pais no se encuentra en la base de datos")
    return busPais2

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

nombre = []
pais = []
fecha = []

for i in personas:
    n=i.split(',')
    nombre.append(n[0])
    pais.append(n[1])
    fecha.append(n[2])

busPais = "Argentina"
cuentaPais = 0
print("En la base de Datos hay ", cuentaCantidad (pais,busPais), "de ", busPais)
busPais2 = (valid (pais))

print("En la base de Datos hay ", cuentaCantidad (pais,busPais2), "de ", busPais)


