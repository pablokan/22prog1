def saludo(nombre, edad):
    print(f"Hola {nombre}, tenés {edad} años")

saludo("José", 33)

persona = ("Juan", 17)

saludo(persona[0], persona[1])
saludo(*persona)
