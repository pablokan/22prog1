# Pedir el ingreso de un nombre completo (Juan Pérez) y mostrarlo invertido y con coma (Pérez, Juan).

def invertirNombre(nombreCompleto): # con find
    posEspacio = nombreCompleto.find(" ")
    ape = nombreCompleto[posEspacio+1:]
    nom = nombreCompleto[:posEspacio]
    return ape + ", " + nom

def invName(nameStr):
    l=nameStr.split()
    return l[1]+', '+l[0]

k='Hector Gonzalez'
print(invName(k))    

print(invertirNombre("Pablo Kaniefsky"))
print(invertirNombre("Juanita Torres"))

