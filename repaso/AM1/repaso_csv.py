a = open("pruebas/repaso.csv")
personas = a.readlines()

for persona in personas:
    persona = persona[:-1]
    nombre, edad, salario = persona.split(",")
    print(f"Nombre: {nombre}. Edad: {edad}. Salario: {salario}")
