personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(America),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-04-2001",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(Europe),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-03-2002"
]

for x in range(len(personas)):
    personas[x] = personas[x].split(",") # divide cada ítem por las comas
                                         # esto es de tal manera que personas[x][1] es el país&continente, etc

# 1) Los apellidos de las personas nacidas antes de un año solicitado al usuario.

def getyearofbirth(searchY): # searchY es el año a buscar (Y = year)
    personasAño = ""
    personasApellido = ""
    searchY = int(searchY)
    for x in range(len(personas)):
        personasAño = int(personas[x][2][6:]) # personas[x][2] es la fecha de nacimiento
                                              # después del carácter 6 siempre está el año! (11-22-3333)
                                                                                            #123456
        if searchY > personasAño:
            personasApellido = personas[x][0].split(" ") # divide el nombre en nombre y apellido
            print(personasApellido[1]) # printea el apellido

getyearofbirth(input("Escriba Año por Buscar (e.j. 1991):"))

print("------------------------------------------------")

# 2) La cantidad de personas nacidas en  Norway

def getcountry(searchC): # searchC es el país a buscar (C = country)

    count = 0
    
    for x in range(len(personas)):
        personasCountry = personas[x][1].split("(") # personas[x][1] es el país&continente
                                                    # personasCountry[0] es el país y [1] continente
        if searchC in personasCountry[0]:
            count += 1
    
    try: 
        10 / count # si el país es inválido, count siempre == 0, lo cual causa una excepción
        print("La cantidad de personas en", searchC, "es igual a:", count)
    except:
        print("País inválido!")


getcountry("Norway")

print("------------------------------------------------")

# 3) La cantidad de personas de un país ingresado por el usuario 

getcountry(input("Ingrese País [Opciones: 'Germany', 'Norway', 'United States', 'Argentina', 'France']: "))