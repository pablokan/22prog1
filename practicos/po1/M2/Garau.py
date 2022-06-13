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
def busquedaPais(lista, busqueda):
    contador = 0
    for x in range(len(lista)):
        if busqueda in lista[x]:
            contador += 1
    return contador
def inputPais (cartel):
    paisesAdm = "Germany, United States, Norway y France."
    validado = False
    pais = ""
    while not validado:
        pais = input(cartel)
        if pais in paisesAdm:
            validado = True
        else:
            validado= False
            print("El pais no esta admitido en la lista a buscar, las opciones son: Germany, United States, Norway y France. Si ingreso alguno de estos, corrobore que esta bien escrito")
    return pais
def busquedaNacimiento (list, inicial):
    nacimientos = []
    cont = 0
    aux = []
    pos = 0
    for x in range(len(list)):
        aux = list[x].split(",")
        pos = aux[0].rfind(" ")
        apellido = aux[0][pos + 1:]
        if apellido[0] == inicial:
            cont += 1
            nacimientos.append(aux[2])
    print ("Hay", cont, "personas cuyo apellido comienza con", inicial, "sus nacimientos son:", nacimientos)
def validarCaracter(cartel,val1, val2):
    validado = False
    caracter = ""
    while not validado:
        caracter = input(cartel)
        codigo = ord(caracter)
        if codigo >= val1 and codigo <= val2:
            validado = True
        else:
            print("El caracter ingresado es invalido, intente nuevamente: ")
    return caracter

print("La cantidad de personas de Argentina en la lista son:", busquedaPais(personas, "Argentina"))
pais = inputPais("Ingrese un pais a buscar en la lista: ")
print ("Hay", busquedaPais(personas, pais), "personas que son de", pais)
inicial = validarCaracter("Ingrese una letra Mayuscula: ", 65, 90)
busquedaNacimiento(personas, inicial)
