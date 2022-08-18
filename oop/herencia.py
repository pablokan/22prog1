class Animal():
    def __init__(self, nombre):
        self.nombre = nombre

    def obtenerNombre(self):
        return self.nombre

    def habla(self):
        return "No se que decir"

class Gato(Animal): # Gato hereda Animal 
    def __init__(self, nombre, dieta):
        Animal.__init__(self, nombre)
        self.dieta = dieta

    def habla(self): # polimorfismo
        return "miauuu"

kitty = Gato("Kitty", "carnívora")
print(kitty.habla())
print(kitty.obtenerNombre())

class Perro(Animal):
    def __init__(self, nombre, dieta):
        Animal.__init__(self, nombre)
        self.dieta = dieta

    def habla(self): # polimorfismo
        return "guauuu"

timmy = Perro("Timmy", "lechuga")
print(timmy.habla())