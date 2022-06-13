def cantPais(paises,pais):
    contador=0
    for x in range(len(paises)):
        if paises[x]==pais:
            contador+=1
    return  contador
def validarPaises():
    pais=""
    while pais !="Germany" and  pais !="United States" and  pais !="Norway" and  pais != "France":
        pais=input("Dame un pais de los posibles(Germany, United States, Norway, o France):")
        if pais !="Germany" and  pais !="United States" and  pais !="Norway" and  pais != "France":
            print("El pais seleccionado no es válido.")
    return pais
def fechaNacimiento(nombres,fechas):
    primeraL=input("Dame una letra:")
    fechasN=[]
    for x in range(len(nombres)):
        posicion=nombres[x].find(" ")
        apellido=nombres[x][posicion:]
        if apellido[1]==primeraL:
            fechasN.append(fechas[x])
    return fechasN




lista=["Vikki Tewkesbury,France,30-01-2000",
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
listaNombres=[]
listaPaises=[]
listaFechas=[]

for x in range (len(lista)):
    splitLista=lista[x].split(",")
    listaNombres.append(splitLista[0])
    listaPaises.append(splitLista[1])
    listaFechas.append(splitLista[2])


print("La cantidad de personas de Argentina es:",cantPais(listaPaises,"Argentina"))
print("La cantidad de personas del pais seleccionado es:", cantPais(listaPaises,validarPaises()))
fechas=fechaNacimiento(listaNombres,listaFechas)
print("Las fechas de nacimiento de las personas cuyo apellido comienza con la letra seleccionada son:")
for i in range(len(fechas)):
    print(fechas[i])