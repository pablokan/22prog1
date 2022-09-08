recienLlego = True
saludo = "hola" if recienLlego else "chau"
print(saludo)

def otroSaludo():
    recienLlego = False
    return "hola" if recienLlego else "chau"
print(otroSaludo())

edad = 12
mayorEdad = True if edad >= 18 else False
print(mayorEdad)

hay = "no"
print("si hay algo") if hay == "si" else print("nada")
