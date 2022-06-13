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

nombres = []
paises = []
fechaNac = []

for i in personas:
    l = i.split(",")
    nombres.append(l[0])
    paises.append(l[1])
    fechaNac.append(l[2])



def  buscarPais(list,paisbuscado):
    contador = 0    
    for i in range(len(list)):
        if  paises[i]  == paisbuscado:
            contador += 1
                      
    return "El pais " + paisbuscado + " buscado en la lista aparece " + str(contador) + " veces"

buscador1 = input("introduzca uno de los paises a buscar (Argentina/Germany/United States/Norway/France): ")
print(buscarPais(paises,buscador1))

buscador2 = input("introduzca uno de los paises a buscar (Argentina/Germany/United States/Norway/France): ")
print(buscarPais(paises,buscador2))



