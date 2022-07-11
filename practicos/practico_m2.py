nombres = [
        "Ana Torres",
        "Kate Hudson",
        "Benicio Quesada",
        "Susana Campoamores",
        "Carlos Santamaría",
        "Azul Skarsgard",
        "Walter Catalejos"
]
sexos = ["f","f","m","f","m","f","m"]
fechas = [
    "02/05/1943",
    "07/09/1984",
    "10/02/1971",
    "21/12/1967",
    "18/07/1959",
    "30/08/1995",
    "30/01/1982"
]
print("1) Apellidos luego coma luego nombre")
for x in range(len(nombres)):
    nombre = nombres[x]
    posEspacio = nombre.find(" ")
    apellido = nombre[posEspacio+1:]
    nombre = nombre[:posEspacio]
    nombreCompleto = apellido + ", " + nombre
    print(nombreCompleto)

print("2) Nombre del varón mas viejo")
edadMayor = 0
for i in range(len(sexos)):
    if sexos[i] == "m":
        nombre = nombres[i]
        posEspacio = nombre.find(" ")
        nombre = nombre[:posEspacio]
        # fechaNac = fechas[i]
        dN = int(fechas[i][:2]) # 10/02/1971
        mN = int(fechas[i][3:5])
        aN = int(fechas[i][6:])
        edad = 2022 - aN
        if (mN > 5) or (mN == 5 and dN > 12):
            edad -= 1
        if edad > edadMayor:
            edadMayor = edad
            masViejo = nombre
print("El señor mas anciano es:", masViejo)

print("3) Mostrar el apellido mas largo")
maximo = 0
for i in range(len(nombres)):
    nombre = nombres[i]
    posEspacio = nombre.find(" ")
    apellido = nombre[posEspacio+1:]
    if len(apellido) > maximo:
        maximo = len(apellido)
        largo = apellido
print(largo)
