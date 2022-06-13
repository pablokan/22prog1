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

def contadorPais(pais):
    contador = 0
    for i in range(len(personas)):
        persona = personas[i]
        if pais in persona:
            contador += 1
    return contador

def buscarPais(opcionesPais):
    print("Opciones",opcionesPais)
    validado = True
    while validado:
        paisIngresado = input("Ingrese otro pais ademas de Argentina: ")
        if paisIngresado in opcionesPais:
            validado = False
            return contadorPais(paisIngresado),paisIngresado
        else:
            print("Opcion Invalida")        

def fechaPorLetraDeApellido(cartel):
    fechasDeNacimiento = []
    letra = input(cartel)
    for i in range(len(personas)):
        persona = personas[i].split(',')
        apellido = persona[0].split()
        if letra == apellido[1][0]:
            fechasDeNacimiento.append(persona[2])
    return fechasDeNacimiento,letra


print('La cantidad de personas de Argentina son:',contadorPais('Argentina'))
print('-------------------')
cantPersonas,pIngresado = buscarPais(['Germany', 'United States', 'Norway', 'France'])
print("La cantidad de Personas de",pIngresado,"es",cantPersonas)
print('-------------------')
fechasDeNacimiento,letra = fechaPorLetraDeApellido('Ingrese inicial de una apellido en mayuscula: ')
print('Las fechas de nacimiento de las personas cuyo apellido empieza con',letra,'son',fechasDeNacimiento)


    