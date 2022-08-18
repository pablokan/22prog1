class Animal:
    def __init__(self, n):
        self.name = n

    def habla(self):
        return "No sé que decir"

class Gato(Animal): # Gato hereda Animal
    def __init__(self, n, f): # constructor de Gato
        super().__init__(n) # llama al constructor de Animal
        self.familia = f

    def habla(self): # polimorfismo: sobreescribe el método de la clase madre Animal
        return "miauuuuu"

class Perro(Animal):
    def __init__(self, n, f):
        super().__init__(n)
        self.familia = f

michi = Gato("Jerry", "leones")
print(michi.name, michi.familia, michi.habla())

bobby = Perro("Bobby", "lobos")
print(bobby.name, bobby.habla())

