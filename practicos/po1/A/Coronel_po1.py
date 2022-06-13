#Quiero obtener:
#La cantidad de personas de Argentina
#La cantidad de personas de un país ingresado por el usuario 
#Las fechas de nacimiento de las personas cuyo apellido comience con una letra solicitada al usuario
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
nombres=[]
paises=[]
fechas=[]

for i in personas:
    n=i.split(",")
    nombres.append(n[0])
    paises.append(n[1])
    fechas.append(n[2])
cantidadArgentos=0
for x in paises:
    if x== "Argentina":
        cantidadArgentos+=1
print("La cantidad de personas de Argentina es", cantidadArgentos)

argentinos=0
franceses=0
gringos=0
noruegos=0
pais= input ("ingrese un pais:")
while pais in paises:
    if pais== "Argentina":
        argentinos+=1
    if pais== "Norway":
        noruegos+=1
    if pais== "United States":
        gringos+=1
    if pais== "France":
        franceses+=1
    pais=input("ingrese un pais:")
paisrequerido=input("ingrese el nombre  del pais cuya cantidad de nativos quiere saber:")
if paisrequerido=="Argentina":
    print("La cantidad de argentinos es",argentinos)
if paisrequerido== "Norway":
    print("La cantidad de noruegos es", noruegos)
if paisrequerido=="United States":
    print("La cantidad de Estadounidenses es",gringos)
if paisrequerido== "Frances":
    print("La cantidad de franceses es",franceses)

