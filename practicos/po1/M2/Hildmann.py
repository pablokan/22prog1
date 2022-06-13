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
#actividad 1
def personasporpais(paises="Argentina"):
    contador=0
    for x in range(len(personas)):
        unidad = personas[x]
        unidad=unidad.split(",")
        if unidad[1] == paises:
            contador += 1
    return contador
 
print("la cantidad de personas que viven en argentina son:",personasporpais())

#actividad 2

def continente():
    validado=False
    while not validado:
        A=input("ingrese el pais: ")
        try:
            if A in ['Germany', 'United States', 'Norway', 'France']:
                validado=True
                return A
        except:
            print("ingrese un pais existente")
pais=continente()
print("la cantidad de personas que viven en:",pais,"son un total de:",personasporpais(pais))

#actividad 3

letra=input("ingrese la incial del apellido que desa buscar: ")
def buscadorfechas(letrita):
    nombres=[]
    fechas=[]
    for x in range (len(personas)):
        individuo=personas[x]
        individuo=individuo.split(",")
        posicion=individuo[0].find(" ")
        if (individuo[0][posicion+1:posicion+2])==letrita:
            nombres.append(individuo[0])
            fechas.append (individuo[2])
    print("las personas con appellido empezado en:",letra,"con sus repectivas fechas de nacimiento son: ")
    for i in range (len(nombres)):
        print(nombres[i],fechas[i])

buscadorfechas(letra)