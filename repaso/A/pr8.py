from datetime import date

archivo = open("repaso/B/nacidos.csv")
aP = 1999

filas = archivo.readlines()
filas.pop(0)
for fila in filas:
    pC = fila.find(",")
    aN = int(fila[pC+1:pC+5])
    mN = int(fila[pC+6:pC+8])
    dN = int(fila[pC+9:pC+11])
    fechaNac = date(aN, mN, dN)
    inicioVerano = date(aP-1, 12, 21)
    finVerano = date(aP, 3, 20)
    if inicioVerano <= fechaNac <= finVerano:
        print(fila[:-1])