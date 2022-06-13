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
pais = []
fecha = []

def cantidadPersonas(lista):
    for i in lista:
        if 'Argentina' in i:
            contadorArg+=1
for x in personas:
    coma = x.split(",")
    nombres.append(coma[0])
    pais.append(coma[1])
    fecha.append(coma[2])

#1
contador = 0
for i in range (len(pais)):
    if pais[i] == "Argentina":
        contador += 1
print ("la cantindad de personas de nacionalidad Argentina es", contador)

#2
validado = False
while not validado:
    pregunta = str(input("Ingrese la nacionalidad a buscar: "))
    if pregunta in pais:
        validado = True
    else:
        print("El pais ingresado no se encuentra, ingrese uno correctamente")

contador2 = 0
for n in range(len(pais)):
    if pais[n] == pregunta:
        contador2 +=1 
print("La cantidad de personas de nacionalidad", pregunta, "es", contador2)

#3
"""validado = False
while not validado:
    inicial_apellido = str(input("Ingrese la letra inicial del apellido a buscar: "))
    print("acontinuación se mostraran las fechas de nacimientos de las personas cuyo apellido comiencen con la letra", inicial_apellido)

for k in range(len(nombres)):
    espacio = nombres[k].find(" ")
    if inci in nombres[k][espacio:espacio+1]:
        print(fecha[k])
    else:
        inicial_apellido in nombres
        validado == True

print("Los apellidos de la lista no contienen la letra",inicial_apellido)
"""