personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-04-2001",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-03-2002"
]

aP = 2000
apellidos = []
# for x in range(len(personas)):
#     persona = personas[x]
for persona in personas: # para cada persona en la lista personas
    listaPersona = persona.split(",")
    nombreCompleto = listaPersona[0]
    pais = listaPersona[1]
    fecha = listaPersona[2]
    aN = int(fecha[6:])
    nombreLista = nombreCompleto.split()
    apellido = nombreLista[1]    
    if aN < aP:
        apellidos.append(apellido)


for apellido in apellidos:
    print(apellido)
    
