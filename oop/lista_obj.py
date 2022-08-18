class Persona:
    def __init__(self, n, a):
        self.nombre = n
        self.altura = a

    def __str__(self):
        return f"Me llamo {self.nombre} y mido {self.altura}"

listaPersonas = []

for i in range(3):
    nom = input("Nombre: ")
    alt = float(input("Altura: "))
    p = Persona(nom, alt)
    listaPersonas.append(p)

for persona in listaPersonas:
    print(persona)

