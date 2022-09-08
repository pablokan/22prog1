class Animal:
    def __init__(self, id, peso) -> None:
        self.id = id
        self.peso = peso

    def salud(self):
        pass

class Puma(Animal):
    def __init__(self, id, peso, edad) -> None:
        super().__init__(id, peso)
        self.edad = edad

    def salud(self):
        if (self.peso >= 200):
                r = "sano"
        else:
                r = "enfermo"
        return r
        
    def adulto(self):
        if self.edad > 5:
            return True
        else:
            return False

class Venado(Animal):
    def __init__(self, id, peso) -> None:
        super().__init__(id, peso)

    def salud(self):
        if (self.peso >= 120):
                r = "sano"
        else:
                r = "enfermo"
        return r

animalito = Puma(1, 230, 11)
otroAnimalito = Venado(1, 100)

print(animalito.peso)
print(otroAnimalito.peso)
