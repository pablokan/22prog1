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

#1--------La cantidad de personas de Argentina---------
def contador_Personas(paises):
    contador=0
    for x in range(len(personas)):
        pers = personas[x]
        pers=pers.split(",")
        if pers[1] == paises:
            contador += 1
    return contador

print("La cantidad de personas en Argentina: " ,contador_Personas("Argentina"))

#2---------La cantidad de personas de un país ingresado por el usuario-------
pais=input("ingrese pais: ")
def validado_Personass(paises):
    contador=0
    obligado=["Argentina, Germany, United States, Norway, France"]
    validado= False
    for x in range(len(personas)):
        pers = personas[x]
        pers=pers.split(",")
        try:
            if pers[1] == paises and pers[1]==obligado:
                contador += 1
                validado = True
        except:
            print("El pais ingresado es incorrecto!, intente nuevamente")
    return contador
print("La cantidad de personas en el pais ingresado es: ", validado_Personass(pais))

#3---------Las fechas de nacimiento de las personas cuyo apellido comience con una letra solicitada al usuario-------
inicial=input("ingrese la incial del apellido que desea buscar: ")
def nac_fecha(letra):
    apellidos=[]
    fechas=[]
    for x in range (len(personas)):
        pers=personas[x]
        pers=pers.split(",")
        posicion=pers[0].find(" ")
        if (pers[0][posicion+1:posicion+2])==letra:
            apellidos.append(pers[0])
            fechas.append (pers[2])
    return (apellidos, fechas)       
print("Las fechas de nacimiento de las personas cuyo apellido empieza con",inicial,"son:",nac_fecha(inicial))







