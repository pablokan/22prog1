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

#cantidas de personas de Argentina
c=0
for i in range(len(personas)):
    if "Argentina" in personas[i]:
        c += 1
print("la cantidad de personas de Argentina es", c)



#fecha de nacimiento de las personas
acumulador=[]
for x in range(len(personas)):
    personas = personas[x]
    nueva_lista = personas.split(",")
    fecha_nac = nueva_lista[2]
    ingreso= str(input("ingrese letra inicial del nombre de la persona:"))
    if ingreso==nueva_lista[0][:1]:
        acumulador += fecha_nac
print("Las fechas de nacimiento de las personas cuyo apellido empieza con", ingreso, "son: ",acumulador)





    
#cantidad de personas de paises ingresado por usuario
opciones= ["Germany", "United States", "Norway", "France"]
paises=[]
contador = 0
def inputstr(texto, pais="argentina"):
    validado = False
    while not validado:
        try:
            p= inputstr(pais)
            if p == opciones[i]:
                validado= True
                contador = contador + 1
            print("el pais",p, "se conto", contador,"veses")
        except:
            print("Pais no valido")
    return p
inputstr




 