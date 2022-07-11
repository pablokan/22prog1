nombres = ["Juan", "Pedro", "Ana", "Iñaki", "María"]
fechas = ["01/01/2000", "02/02/2010", "12/07/1999", "27/06/2004", "05/05/1980"]

a = open("personas.txt", "w", encoding="utf-8")
a.write("Nombre, Fecha de nacimiento\n")
for i in range(len(nombres)):
    a.write(f"{nombres[i]}, {fechas[i]}\n")
a.close()

