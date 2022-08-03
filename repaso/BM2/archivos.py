

nombres = ["Ana", "Juan"]
fechas = ["02/02/2001", "31/07/1987"]
a = open("repaso/BM2/personas.txt", "a")
for i in range(len(nombres)):
    linea = f"{nombres[i]},{fechas[i]}"
    print(linea)
    a.write(linea + "\n")


a.close()