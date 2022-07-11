# Cargar en listas los nombres 
# y fechas de nacimiento de varias personas,
#  luego recorrerlo y mostrar los nombres 
# de los mayores de edad.

nombres = ["Ana", "Luis", "Juan"]
fecNac = ["13-05-1987", "01-12-2010", "23-01-2001"]

for x in range(len(nombres)):
    diaNac = int(fecNac[x][:2])
    mesNac = int(fecNac[x][3:5])
    aniNac = int(fecNac[x][-4:])
    edad = 2022 - aniNac
    if mesNac > 5 or mesNac == 5 and diaNac > 4:
        edad -= 1
    if edad >= 18:
        print(nombres[x])


