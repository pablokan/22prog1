n = 0

if n > 1:
    # dentro del if se cumple si la condición es verdadera
    print("----- raya de relleno --------")
    print("es mayor que uno")  # indentación
    print("----de nuevo raya de relleno ---------")
else:
    # dentro del else
    # entra por acá si la condición es falsa
    print("la condición es falsa")

print("afuera del if")

# las comparaciones posibles son: <, >, <=, >=, ==, !=
nombre = "Juan"

if nombre == "Juan":
    print("El pibe se llama Juan")

edad = 4

if edad > 0 and edad < 12:  # if 0 < edad < 12
    print("es un niñe")
elif edad >= 12 and edad <= 20:
    print("es un adolescente")
elif edad > 20 and edad < 50:
    print("es un adulto")
else:
    print("es un anciano")
