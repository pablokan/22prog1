#nombre,pais,fecha de nacimiento.
#1)La cantidad de personas de Argentina
#2)La cantidad de personas de un país ingresado por el usuario 
#3)Las fechas de nacimiento de las personas cuyo apellido comience con una letra solicitada al usuario
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

def validacionPaises(paises):
    validado=False
    while not validado:
        print('opciones:', paises)
        pais=input('Ingrese un país de los anteriores:')
        if pais in paises:
            validado=True
            return pais
        else:
            print('Ese país no es válido.')
            print('')

def Pais(paisesdisponibles):
    c=0
    for x in range(len(personas)):
        persona=personas[x].split(',')
        if persona[1]=="Argentina":
            c+=1
    print('La cantidad de personas de Argentina es:',c)
    print('')
    c2=0
    pais2=validacionPaises(paisesdisponibles)
    for y in range(len(personas)):
        persona=personas[y].split(',')
        if persona[1]==pais2:
            c2+=1
    print('la cantidad de personas de',pais2,'es:',c2)
    return c, c2 #no se usa
 
def contarApellido(mensaje):
    inicial=input(mensaje)
    print('las personas cuyo apellido empieza con',inicial+', si las hay, son:')
    for a in range(len(personas)):
        persona=personas[a].split(',')
        pos=persona[0].find(' ')
        if inicial in persona[0][pos+1:pos+2]:
            print(persona[2])

Pais(['Argentina', 'United States', 'Norway', 'France'])
print('')
contarApellido('ingrese inicial mayúscula del apellido a buscar:')