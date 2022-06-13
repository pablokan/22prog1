
def personasAnioSolicitado(pnas, anioSolicitado=2000): # Los apellidos de las personas nacidas antes de un año solicitado al usuario
    nombresCompletos = []
    paises = []
    fechasNacimiento = []
    apellidos = []
    anios = []
    apellidosMenorAnio = []
    for i in range(len(pnas)): # Divido en listas paralelas los 3 datos recibidos
        nombre, pais, nacimiento = pnas[i].split(",")
        nombresCompletos.append(nombre)
        paises.append(pais)
        fechasNacimiento.append(nacimiento)
    
    for i in range(len(nombresCompletos)): # Sacar los apellidos de la lista de los nombres completos con un find
        espacioNombres = nombresCompletos[i].find(" ")
        apellidos.append(nombresCompletos[i][espacioNombres+1:])
    
    for i in range(len(fechasNacimiento)): # Busco los años de nacimiento segun los guiones con un rfind
        guionAnio = fechasNacimiento[i].rfind("-")
        anio = fechasNacimiento[i][guionAnio+1:]
        anios.append(int(anio))
    
    for i in range(len(apellidos)): # Segun el año solicitado agrego a una lista las personas que hayan nacido antes de ese año.
        if anios[i] < anioSolicitado:
            apellidosMenorAnio.append(apellidos[i])
    return apellidosMenorAnio

def personasNacidasSegunPais(pnas, paisElegido = "Norway"):
    nombresCompletos = []
    paisesContinentes = []
    fechasNacimiento = []
    paises = []
    cantPersonasPaisElegido = 0
    for i in range(len(pnas)): # Divido en listas paralelas los 3 datos recibidos
        nombre, pais, nacimiento = pnas[i].split(",")
        nombresCompletos.append(nombre)
        paisesContinentes.append(pais)
        fechasNacimiento.append(nacimiento)

    for i in range(len(paisesContinentes)): # Busco el parentesis para sacar el continente y quedarme con el pais
        parentesis = paisesContinentes[i].find("(")
        paises.append(paisesContinentes[i][:parentesis])

    for i in range(len(paises)): # verifica si el pais elegido es igual a algun pais de la lista y lo acumula
        if paises[i] == paisElegido:
            cantPersonasPaisElegido += 1
    print("La cantidad de personas de " + paisElegido + " es de: ", cantPersonasPaisElegido)

def validacionPais(paisElegido): # Validar si el pais elegido esta dentro de las opciones
    paisesPosibles = ('Argentina', 'France', 'Norway', 'United States', 'Germany')
    while paisElegido not in paisesPosibles:
        paisElegido = input("Opcion inválida vuelva a intentarlo: ")
    return paisElegido
    
def main():
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

    anioS = int(input("Ingrese un año: "))
    personasMenores = personasAnioSolicitado(personas, anioS)
    print("Las personas menores al año solicitado son: ", personasMenores)
    
    print("Opciones de paises: 'Germany', 'Norway', 'United States', 'Argentina', 'France'")
    paisEleg = input("Ingrese un pais valido: ")
    personasNacidasSegunPais(personas, validacionPais(paisEleg))

if __name__ == "__main__":
    main()