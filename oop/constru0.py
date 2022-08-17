class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Este gatito se llama {self.nombre} y tiene {self.edad} años"


kitty = Gato("Kitty", 3)

print(kitty)

