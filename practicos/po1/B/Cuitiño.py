personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-04-2001",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-03-2002"
]


#Ejercicio 1
def personasNacidas(añoSolicitado):
    print("Las personas nacidas antes del", añoSolicitado, "son: ")
    for i in range(len(personas)):
        persona = personas[i]
        datosPersona = persona.split(",")
        fechaNaci = datosPersona[-1].split("-")
        añoNaci = int(fechaNaci[2])
        nombreCom= datosPersona[0].split(" ")
        apellido = nombreCom[1]
        if añoNaci < int(añoSolicitado):
            print(apellido)


def cantPers(paisSolicitado):
    cont = 0
    for x in range(len(personas)):
        persona = personas[x]
        datosPersona = persona.split(",")
        lugarNaci = datosPersona[1]
        posParentesis = lugarNaci.find("(")
        pais = lugarNaci[:posParentesis]
        if pais == paisSolicitado:
            cont +=1
    return cont

def validarOpcion(lista):
    opcion = input("Ingrese uno de los paises aceptados: ")
    validado = False
    while not validado:
        if opcion in lista:
            validado= True
        else:
            print ("Opcion Invalida")
            opcion = input("Ingrese uno de los países aceptados: ")
    return opcion


if __name__ == "__main__":
    # ejercicio 1
    año =input("Ingrese año: ")
    personasNacidas(año)
    #Ejercicio 2
    personasNorway = cantPers("Norway")
    print("Las personas nacidas en Norway son: ", personasNorway)
    #Ejercico 3
    Opciones= ["Germany", "Norway", "United States", "Argentina", "France"]
    pais= validarOpcion(Opciones)
    personas = cantPers(pais)
    print("La cantidad de personas de ", pais, "son: ", personas)