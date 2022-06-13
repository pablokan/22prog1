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

def contarPais(personas, pais= 'Argentina'):
    if pais != 'Argentina':
        validado = False
        while not validado:
            if pais in paisesValidos:
                validado = True
            else:
                pais = input('El pais no esta en la lista, ingrese otro ').title()
    c = 0
    for persona in personas:
        datos = persona.split(',')
        if datos[1] == pais:
            c += 1
    print('Hay ' + str(c) + ' personas de ' + pais)

contarPais(personas)
paisesValidos = ['Germany', 'United States', 'Norway', 'France']
print('Los paises para buscar son:' + str(paisesValidos))
otroPais = input('De cual pais quiere buscar la cantidad de personas? ').title()
contarPais(personas, otroPais)

def buscarNacimientos(personas, letra):
    for persona in personas:
        posicionApellido = persona.find(' ') #El primer espacio separa al nombre del apellido
        letraApellido = persona[posicionApellido +  1] #La posicion siguiente al espacio sera la primer letra del apellido
        datos = persona.split(',')
        if letra == letraApellido:
            print(datos[2])

letraBusqueda = input('Que apellido quiere buscar fechas de nacimiento? ').upper() #Transformo la letra a mayuscula por si se ingresa una minuscula
buscarNacimientos(personas, letraBusqueda)