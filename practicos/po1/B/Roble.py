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




def NacidosAntes():
    año = input('ingrese el año que desee buscar(aaaa): ')
    listPersonas = []
    apellidos = []
    for x in range(len(personas)):
        persona = personas[x].split(',')
        listPersonas.append(persona)
        añoN = listPersonas[x][2][6:10]
        if añoN < año:
            espacio = listPersonas[x][0].find(' ')
            apellido =  listPersonas[x][0][espacio+1:]
            apellidos.append(apellido)
    print ("Los apellidos de las personas nacidas antes del año ",año, 'son: ')
    for x in range(len(apellidos)):
        print(apellidos[x])

NacidosAntes()

def Nacionalidad(ingreso):
    cantidad = 0
    listPersonas = []
    opciones = []
    for x in range(len(personas)):
        persona = personas[x].split(',')
        listPersonas.append(persona)
        parentesis = listPersonas[x][1].find('(')
        pais = listPersonas[x][1][:parentesis]
        opciones.append(pais)
    valido = False
    while not valido:
        paisUsuario = ingreso
        if paisUsuario in opciones:
            for x in range(len(personas)):
                if paisUsuario == opciones[x]:
                    cantidad += 1
            valido = True
        else:
            print('Opcion Invalida')
            valido = True
    print ('La cantida de personas nacidas en',paisUsuario, 'son:', cantidad)
 
Nacionalidad('Norway')

print('Opciones: Germany, Norway, United States, Argentina, France')
paisIngresado = input('Ingrese uno de los países aceptados: ')

Nacionalidad(paisIngresado)