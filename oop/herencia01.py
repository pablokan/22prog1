class Animal:
    def setName(self, n):
        self.name = n

class Gato(Animal): # Gato hereda Animal
    pass

michi = Gato()
michi.setName("Michi")

print(michi.name)
