class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"

personita = Persona("Juan", 33)
print(personita.nombre)
otraPersona = Persona("Ana", 88)
print(otraPersona)

