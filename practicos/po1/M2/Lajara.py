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
    "Ambrosio Cadore,Norway,09-12-2002"]

def CantPerPais(Pais,Pers):
    Contador = 0
    ListPersona = Pers    
    if Pais == "Argentina" :
        for i in range(len(ListPersona)):
            Listx = ListPersona[i].split(",")                
            if  "Argentina" in Listx[1]:            
                Contador = Contador + 1
    else:
        Opciones= ['Germany', 'United States', 'Norway', 'France']
        validar = 0
        while validar == 0:            
            if Pais in Opciones:
                for i in range(len(Opciones)):            
                    if  Pais in Opciones[i]: 
                        for i in range(len(ListPersona)):
                            Listx = ListPersona[i].split(",")                
                            if  Pais in Listx[1]:            
                                Contador = Contador + 1
                                validar = 1
            else:
                Pais = input("Ingrese otro país además de " + Pais + " : ")                                
    return Contador,Pais

def BuscarApeLetra(Letra,Pers):
    ListPersona = Pers 
    Lista2 = []    
    for i in range(len(ListPersona)):
            Listx = ListPersona[i].split(",")                            
            if  Letra in Listx[0][1:]:
                Lista2.append(Listx[2])          
    print("Las fechas de nacimiento de las personas cuyo apellido empieza con ",Letra," son:") 
    return Lista2

Var = CantPerPais("Argentina",personas)
print("La cantidad de personas de Argentina es", Var[0])

Var = CantPerPais(input("Ingrese Pais: "),personas)
print("La cantidad de personas de ",Var[1]," es", Var[0])

Var = BuscarApeLetra(input("Ingrese inicial de apellido: "),personas)
for i in range(len(Var)):
    print(Var[i])