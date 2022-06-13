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
    "Ambrosio Cadore,Norway,09-12-2002"]

def cantidadPersonas (paisBuscado):
    c=0
    for x in range (len(personas)):
        if paisBuscado in personas[x]:
            c+=1

    return c
print ("La cantidad de personas de Argentina es ", cantidadPersonas("Argentina"))

paises= ['Germany', 'United States', 'Norway', 'France']
def restrinccion (paisBuscado):
    validado = False
    while not validado:
        pais= input("Ingrese el país que desea buscar: ")
        if pais in paises:
            validado = True
        else:
            print("Opción inválida")
    
    return pais


paisBuscado= input("Ingrese el país que desea buscar: ")

print ("La cantidad de personas de", paisBuscado, "es",  cantidadPersonas(paisBuscado))

letra=input("Ingrese la letra que desea buscar: ")
def fechaNac (letra):
    for x in range (len(personas)):
        persona = personas [x]
        p=persona.replace(" ", ",")
        print (p)

 #se que tengo que buscar la posicion del apellido, comparar la primer letra y mandar la posicion de la fecha
 # pero no me sale :(     


