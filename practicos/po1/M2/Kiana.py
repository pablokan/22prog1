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

def contadorArgentina(personas):
    cantidadper=0
    for x in range (len(personas)):
        if "Argentina" in personas[x]:
            cantidadper +=1
print("La cantidad de personas en Argentina: ",contadorArgentina(personas)
#antes de hacerlo funcion me daba 3 pero no se que hice mal para que no lo printee
#ni cuando llamo a la funcion printeando.




#La cantidad de personas de un país ingresado por el usuario 
paisconacceso=input("Ingrese uno de los paises con acceso: Germany, United States, Norway, France: ")
contadorPais=0
def cantidadPersonas(personas,numero):
    for x in range(len(personas)):
        if paisconacceso in personas:
            contadorPais +=1
        else:
            print("No es valido")
    print("La cantidad de personas en los paises permitidos ingresados es :", contadorPais)

print(cantidadPersonas)
print("---------------------------------------------------------------------------------------")

#Las fechas de nacimiento de las personas cuyo apellido 
# comience con una letra solicitada al usuario

#for x in range(len(personas)):
   # nombres= len(personas)[0:","]
    #if [x] == nombres:
      # print (nombres[x])

#for x in personas:
    #if x == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
      #  personas= personas.pop[0:1]
       # print(personas[x]) #nno sale


letra = input("Ingrese una letra: ")

for x in range (len(personas)):
    if letra == personas[x][0:1]:
    
        print(personas[x])
        
