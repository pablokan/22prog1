# 1) La cantidad de personas de Argentina
# 2) La cantidad de personas de un país ingresado por el usuario 
# 3) Las fechas de nacimiento de las personas cuyo apellido comience con una 
#     letra solicitada al usuario
# Hector Gonzalez

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

def cantidadPersonas(lista):
    contadorArg=0
    for i in lista:
        if 'Argentina' in i:
            contadorArg+=1

    strpais=input('Ingrese uno de los siguientes paises (France, Norway, United States): ')
    while strpais.lower()!='france' and strpais.lower()!='norway' and strpais.lower()!='united utates':
        print('El Pais Ingresado no es valido, vuelva a intentarlo. ')
        strpais=input('Ingrese uno de los siguientes paises (France, Norway, United States): ')
    contadorPaisIngresado=0
    for j in lista:
        if strpais in j.lower():
            contadorPaisIngresado+=1
    return contadorArg, contadorPaisIngresado



a=cantidadPersonas(personas)
print('La cantidad de personas de Argentina es: ',a[0])
print('La cantidad de personas del pais ingresado es: ',a[1])

def fechas(lista1):
    abcd=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    inicialApellido=input('Ingrese la inicial del apellido para obtener la F.N: ')
    inicialApellido=inicialApellido.upper()
    while not inicialApellido in abcd:
        print('La inicial no es valida, vuelva a intentar.')
        inicialApellido=input('Ingrese la inicial del apellido para obtener la F.N: ')
        inicialApellido=inicialApellido.upper()

    listaFechas=[]
    for k in lista1:
        l=k.split(',')
        l1=l[0].split()
        if l1[1][0]==inicialApellido:
            listaFechas.append(l[2])
    return listaFechas

g1=fechas(personas)
print(g1)

