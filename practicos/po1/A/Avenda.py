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

nombresApellidos=[]
pais=[]
fecha=[]

for x in personas:
    personas=x.split(",")
    nombresApellidos.append(personas[0])
    pais.append(personas[1])
    fecha.append(personas[2])

#Cantidad de personas de Argentina.

contador=0

for x in range (len(pais)):
    if pais[x]=="Argentina":
        arg=pais[x]
        contador +=1
print("La cantidad de personas de la lista que son de",arg,"es",contador)

#Cantidad de personas de un país ingresado por el usuario.

ingreso=input("Ingrese país que desee buscar en la lista: ")

contadorA=0
paises=[]

for x in range(len(pais)):
    if pais[x]==ingreso:
        contadorA +=1
print("La cantidad de personas ingresadas en la lista que son de",ingreso,"es",contadorA)

#Las fechas de nacimiento de las personas cuyo apellido comience con una letra solicitada al usuario.

apellidos=[]

letra=input("Ingrese una letra: ")

for x in range (len(nombresApellidos)):
    corte=nombresApellidos[x].find(" ")
    apellido=nombresApellidos[x][corte+1:]
    apellidos.append(apellido)

nacimientoMismaLetra=[]

for x in range (len(apellidos)):
    if apellidos[x][0]==letra.upper():
        nacimientoMismaLetra.append(fecha[x])
print(nacimientoMismaLetra)

