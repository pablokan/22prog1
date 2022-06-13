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


def buscar(PersonasParametro):
    noruegos = 0
    for x in range(len(PersonasParametro)):
        Persona = PersonasParametro[x]              # asigno a Persona el valor de la posicion x de la lista
        Persona = Persona.split(',')                # separo la cadena de caracteres por comas
        Parentesis = Persona[1].find('(')           # busco la posicion del parentesis
        if Persona[1][:Parentesis] == 'Norway':     # si el pais es noruego
            noruegos +=1                            # sumo 1 al contador de noruegos
    
        Pais = Persona[1]                           
        Parentesis = Pais.find('(')
        Pais = Pais[:Parentesis]                    
        if Pais not in Paises:                      # si el pais no esta en la lista de paises
            Paises.append(Pais)                     # entonces lo meto 
    print('la cantidad de personas en Norway es', noruegos)

    Contador = 0
    PaisIngresado = inputpais(Paises)             
    for x in range(len(PersonasParametro)): 

        Persona = PersonasParametro[x]              
        Persona = Persona.split(',')
        Parentesis = Persona[1].find('(')
        if PaisIngresado == Persona[1][:Parentesis]:
            Contador += 1
    print( 'la cantidad de personas en',PaisIngresado ,'es' ,Contador )

def inputpais(Paises):
    Validado = False
    while not Validado:
        print('Opciones: ', Paises)
        Pais = input ('ingrese uno de los paises aceptados: ')
        if Pais in Paises:
            Validado = True
            return Pais
        else:
            print('Opcion no valida') 


def BuscarApellido(PersonasParametro):
    Anio = input('ingrese año: ')
    for x in range(len(PersonasParametro)):
        Persona = PersonasParametro[x]              # asigno a Persona el valor de la posicion x de la lista
        Persona = Persona.split(',')                # separo la cadena de caracteres p9r comas
        Nombre = Persona[0]                         # le doy Nombre el valor de la posicion 0 de la lista
        Nombre = Nombre.split(' ')                  # lo transformo en lista para poder separar el apellido
        Apellido = Nombre[1]                        # le doy Apellido el valor de donde se guarda el apellido en la lista

        Fecha = Persona[2]                          # le doy Fecha el valor de donde se encuentra la fecha
        Fecha = Fecha.split('-')                    # lo transofrmo en lista para poder separar el año
        if int(Fecha[2]) < int(Anio):
            print(Apellido)





Paises = []
buscar(personas)
BuscarApellido(personas)