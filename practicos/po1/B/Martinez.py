# Los apellidos de las personas nacidas antes de un año solicitado al usuario.
#En el punto 1) se puede optar en la función que se escriba,
# por retornar o bien imprimir directamente los datos requeridos.

def buscaapellidos(dato, lista,apellidos):
    años = []
    for i in range(len(lista)):
        puente = lista[i].split(",")
        pos = puente[2].rfind("-")
        año = puente[2][pos+1:]
        años.append(año)
    for i in range(len(lista)):
        puente = lista[i].split(",")
        pos = puente[0].find(" ")
        apellido = puente[0][pos+1:]
        if int(años[i]) < dato:
            apellidos.append(apellido)
    return apellidos

def mostrar(lista):
    print("Los apellidos de las personas nacidas antes del 2000 son: ")
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print(" ")

# La cantidad de personas nacidas en  Norway
# La cantidad de personas de un país ingresado por el usuario 
# Para los puntos 2) y 3) se requiere usar la misma función
def validarpais(paises, repeticiones):
    dato = input("Ingrese un pais: ").lower()
    while (dato not in paises):
        print("Opcion no valida - Opciones: ")
        print(repeticiones)
        dato = input("Ingrese un pais: ").lower()
    return dato

def contporpais(lista):
    paises = []
    repeticiones = []
    for i in range(len(lista)):
        puente = lista[i].split(",")
        pos = puente[1].rfind("(")
        pais = puente[1][:pos].lower()
        paises.append(pais)
        if pais not in repeticiones:
            repeticiones.append(pais)
    dato = validarpais(paises,repeticiones)
    contnor = 0
    contdato = 0
    for i in range(len(paises)):
        if paises[i] == "norway":
            contnor = contnor + 1
        if paises[i].lower() == dato.lower():
            contdato = contdato + 1
    if contnor != 0:
        print("La cantidad de personas nacidas en Norway es",contnor)
    else:
        print("No hay personas nacidas en Norway")  
    print("La cantidad de personas nacidas en ",dato," es",contdato)

# Programa principal:
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
año_usuario = int(input("Ingrese un año: "))
apellidos = []
buscaapellidos(año_usuario,personas,apellidos)
if len(apellidos) != 0:
    mostrar(apellidos)
else:
    print("No hay personas nacidas antes del año ",año_usuario)
contporpais(personas)