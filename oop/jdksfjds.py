print(dir("hola"))
class Persona:
    def __init__(self, n, a):
        self.nombre = n
        self.altura = a

    def __str__(self):
        return f"Me llamo {self.nombre} y mido {self.altura}"
p = Persona("J", 0)

print(dir(p))