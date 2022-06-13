# 1) La cantidad de personas de Argentina
# 2) La cantidad de personas de un país ingresado por el usuario 
# 3) Las fechas de nacimiento de las personas cuyo apellido comience con una letra solicitada al usuario

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
fecha = []

for i in personas:
    a = i.split(",")
    nombres.append(a[0])
    paises.append(a[1])
    fecha.append(a[2])

# Funcion 1
def cantidadPersonasXPais(pais):
    c = 0
    for x in paises:
        if x == pais:
            c += 1
    return c

# Ejercicio 1 con funcion
print("La cantidad de personas de Argentina es:", cantidadPersonasXPais("Argentina"))

# Ejercicio 2 con funcion
msg = input("Ingrese el pais de el que desea saber la cantidad de habitantes: ")
def cantidadPersonasXPais(pais):
    cantidadPersonasPais = 0
    for j in paises:
        if j == msg:
           cantidadPersonasPais += 1
    return cantidadPersonasPais
print("La cantidad de personas en", msg, "es:", cantidadPersonasXPais(msg))


# 2 funcion con intento de restriccion, con error :( 

msg = input("Ingrese el pais de el que desea saber la cantidad de habitantes: ")
def cantidadPersonasXPais(pais):
    cantidadPersonasPais = 0
    for j in paises:
        if j == msg:
            cantidadPersonasPais += 1 
            str(cantidadPersonasPais)
        return "La cantidad de personas en " + msg + "es:" + cantidadPersonasPais              
    else:
        print ("Opción inválida")    
print(cantidadPersonasXPais(msg))





