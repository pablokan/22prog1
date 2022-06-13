#Quiero obtener:
#La cantidad de personas de Argentina
#La cantidad de personas de un país ingresado por el usuario 
#Las fechas de nacimiento de las personas cuyo apellido comience con una letra solicitada al usuario

#Para los puntos 1) y 2) se requiere usar la misma función

#Adicionalmente, para el punto 2) se debe restringir el país aceptado en el ingreso a los 4 que existen en el listado además de Argentina, que son Germany, United States, Norway y France. 

#En el punto 3) se puede optar en la función que se escriba, por retornar o bien imprimir directamente los datos requeridos.

#Se esperan 3 funciones!

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
#eje1
nombres=[]
paises=[]
fechadenacimiento=[]
for i in personas:
    n=i.split(',')
    nombres.append(n[0])
    paises.append(n[1])
    fechadenacimiento.append(n[2])

p="Argentina"

def sumaCantidades(pais):
    suma=0
    for k in range(len(paises)):
        if paises [k] == pais:
            suma += 1
        
    return suma
    
print("La cantidad de personas de ese pais:", sumaCantidades(p))

#eje2


c= input("ingrese un pais:")
print (" la cantidad de personas de ese:",sumaCantidades(c))


#eje3

def fechas(nombres):
    abcd=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    inicialApellido=input("Ingrese la inicial del apellido: ")
    inicialApellido=inicialApellido.upper()
    
        
    inicialApellido=input("Ingrese la inicial del apellido: ")
    inicialApellido=inicialApellido.upper()

    listaFechas=[]
    for x in nombres:
        l=x.split(',')
        nombres=l[0].split()
        if nombres[1][0]==inicialApellido:
            listaFechas.append(nombres[0])
    return listaFechas

a=fechas(personas)
print(a)

       
