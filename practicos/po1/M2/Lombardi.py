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

def contadorPersonas(PaisIngresado, paisArg = 'Argentina'):
    contadorArg = 0
    contadorOtro = 0
    for i in range(len(personas)):
        if paisArg in personas[i]:
            contadorArg += 1
        if PaisIngresado in personas [i]:
            contadorOtro += 1
    return contadorOtro, contadorArg

def ingresarPais():
    paisesPermitidos = ['United States','France','Germany','Norway']
    validado = False
    while not validado:
        pais = input('Ingrese un país permitido (United States, France, Norway, Germany): ')
        if pais in paisesPermitidos:
            validado = True
        else:
            print('El país ingresado no está permitido')
    return pais

pais = ingresarPais()
cantidadOtro, cantidadArg = contadorPersonas(pais)

print(f'La cantidad de personas de Argentina son {cantidadArg} y la de {pais} son {cantidadOtro}')

print('---------------------------------------------------------------------------------------------------')

letra = input('Ingrese la letra inicial de los que desea buscar la fecha de nacimiento: ')
#"Willy Branscombe,Argentina,21-11-1997"

def fechasNacimiento(personas,letra):
    listaFechasNacimiento = []
    for i in range(len(personas)):
        indicePrimerEspacio = personas[i].find(' ')
        indicePrimerComa = personas[i].find(',')
        apellido = personas[i][indicePrimerEspacio+1:indicePrimerComa]
        if apellido[:1] == letra:
            indicePrimerGuion = personas[i].find('-')
            fechaNacimiento = personas[i][indicePrimerGuion-2:]
            listaFechasNacimiento.append(fechaNacimiento)
    return listaFechasNacimiento

print(f'Las fechas de nacimiento de las personas cuyo apellido comienza con {letra} son {fechasNacimiento(personas,letra)}')    


