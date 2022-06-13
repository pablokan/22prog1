# Tengo un listado de personas, sus datos son:
# Nombre y Apellido - País de origen (Continente) - Fecha de nacimiento
# Cabral Joel 

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



añoBuscado = int(input("Ingrese un año: "))

for a in (personas):
    j = a.split(",")
    nya = (j[0])
    pais = (j[1])
    fechaNac = (j[2])
    #print(fechaNac[6:])
    aux = nya.split(",")
    aux2 = "".join(aux)
    listaNames = aux2.split()
    apellidoSolo = listaNames[1]
    if añoBuscado > int(fechaNac[6:]):
         print(apellidoSolo)
         
         
         
print("Cantidad de personas que viven en Norway")

for i in range(len(personas)):
    solucion = personas[i]
    if "Norway" in solucion:
        noruegos = solucion.split(",")
print("La cantidad de Norway es: ", (len(noruegos)))



paisBuscado = input("Ingrese el pais que desea buscar, las opciones son: France - United States - Norway - Argentina - Germany: ")
while paisBuscado.lower() != "france" and paisBuscado.lower() != "united states" and paisBuscado.lower() != "norway" and paisBuscado.lower() != "argentina" and paisBuscado.lower() != "germany":
    print("Opcion invalida")
    paisBuscado = input("Ingrese uno de los países aceptados: ") 
cpb = 0
for x in personas:
    if paisBuscado in x.lower():
        cpb += 1
print("La cantidad de personas de", paisBuscado, "es", cpb)





    
# Quiero obtener:
# Los apellidos de las personas nacidas antes de un año solicitado al usuario.
# La cantidad de personas nacidas en  Norway
# La cantidad de personas de un país ingresado por el usuario 

# En el punto 1) se puede optar en la función que se escriba, por retornar o bien imprimir directamente 
# los datos requeridos.

# Para los puntos 2) y 3) se requiere usar la misma función

# Adicionalmente, para el punto 3) se debe restringir el país aceptado en el ingreso
# a los 5 que existen en el listado: Germany, Norway, United States, Argentina y France. 


# Se esperan 3 funciones!


# Salidas esperadas posibles:

# Ingrese año: 2000
# Los apellidos de las personas nacidas antes del 2000 son:
# Brach
# Piffe
# Cleeve
# Milsom

# La cantidad de personas de Norway es 3
# Opciones: ['Germany', 'Norway', 'United States', 'Argentina', 'France']
# Ingrese uno de los países aceptados: Uruguay 
# Opción inválida

# Opciones: ['Germany', 'Norway', 'United States', 'Argentina', 'France']
# Ingrese uno de los países aceptados: Argentina
# La cantidad de personas de Argentina es 2
