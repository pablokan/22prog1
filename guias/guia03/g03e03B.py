nombres = ["Ana", "Luis", "Vilma"]
sexos = ["f", "m", "f"]
mujeres = []

for x in range(len(nombres)):
    if sexos[x] == "f":
        mujeres.append(nombres[x])

print("Los nombres de las mujeres son", mujeres)        