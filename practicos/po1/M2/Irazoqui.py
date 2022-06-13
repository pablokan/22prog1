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

def contadorPersonas(lista,entradaPais):
    c = 0
    for i in range(len(lista)):
        datos = lista[i].split(',')
        if datos[1] == entradaPais:
            c += 1
    return c

def validacionPais(msg):
    validado = False
    while not validado:
        pais = input(msg)
        if pais in ['Germany','United States','Norway','France']:
            validado = True
        else:
            print('Opción Inválida')
    return pais

def fechasNacimiento(lista,letra):
    fechas = []
    letra = letra.upper()
    for i in range(len(lista)):
        datos = lista[i].split(',')
        espacio = datos[0].find(' ')
        apellido = datos[0][espacio+1:]
        if apellido[0] == letra:
            fechas.append(datos[2])
    return fechas

#salidas
if __name__ == '__main__':
#1)
    print('La cantidad de personas en Argentina es',contadorPersonas(personas,'Argentina'))
    print('-'*50)
#2)
    pais = validacionPais('Ingrese otro pais además de Argentina: ')
    print('La cantidad de personas de',pais,'es',contadorPersonas(personas,pais))
    print('-'*50)
#3)
    letra = input('Ingrese una letra: ')
    print('Las fechas de nacimiento de las personas cuyo apellido empieza con',letra,'son:',fechasNacimiento(personas,letra))