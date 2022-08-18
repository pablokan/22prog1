class Persona:
    def __init__(self, n, e) -> None:
        self.nombre = n
        self.edad = e

resp = "si"
lista = []
while resp == "si":
    nom = input("Nombre: ")
    ed = int(input("Edad: "))
    p = Persona(nom, ed)
    lista.append(p)
    resp = input("Hay mas? ")

for persona in lista:
    print(persona.nombre, persona.edad)
