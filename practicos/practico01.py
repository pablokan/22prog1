nombres = ["Torres, Ana", "Hudson, Kate", "Quesada, Benicio", "Campoamores, Susana", "Santamaría, Carlos", "Skarsgard, Azul", "Catalejos, Walter"]
sexos = ["f", "f", "m", "f", "m", "f", "m"]
fecNacs = ["02/05/1943", "07/09/1984", "10/02/1971", "21/12/1967", "30/01/1982", "30/08/1995", "18/07/1959"]

print("1) Mostrar las iniciales de los nombres con apellido completo de todas las personas.")

for x in range(len(nombres)):
    nombre = nombres[x]
    posComa = nombre.find(",")
    inicial = nombre[posComa + 2]
    apellido = nombre[:posComa]
    salida = inicial + ". " + apellido
    print(salida)

print()
print("2) Decir cuál es el nombre de pila más largo.")
masLargo = ""
cantLetras = 0
for x in range(len(nombres)):
    nombre = nombres[x]
    posComa = nombre.find(",")
    nombre = nombre[posComa + 2:]
    if len(nombre) > cantLetras:
        cantLetras = len(nombre)
        masLargo = nombre
print(masLargo)

print()
print("3) El promedio de edad de las mujeres es: ")
totalEdades = 0
cM = 0
for i in range(len(sexos)):
    if sexos[i] == "f":
        cM += 1 
        dN = int(fecNacs[i][:2])
        mN = int(fecNacs[i][3:5])
        aN = int(fecNacs[i][6:])
        edad = 2022 - aN
        if (mN > 5) or (mN == 5 and dN > 9):
            edad -= 1
        totalEdades += edad
print(totalEdades // cM)