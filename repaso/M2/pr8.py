from datetime import date 

archivo = open("repaso/M2/nacidos.csv")
l = archivo.readlines()
aP = 1998
l.pop(0)

for personas in l:
    pC = personas.find(",")
    aN = int(personas[pC+1:pC+5])
    mN = int(personas[pC+6:pC+8])
    dN = int(personas[pC+9:pC+11])
    fechaNac = date(aN,mN, dN)
    veranoInicio = date(aP-1, 12, 21)
    veranoFin = date(aP, 3, 20)
    if veranoInicio <= fechaNac <= veranoFin:
        print(personas[:-1])
