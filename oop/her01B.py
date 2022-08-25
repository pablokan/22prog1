class Animal:
    def setNombre(self, n):
        self.nombre = n

    def habla(self):
        return "no sé que decir"

class Gato(Animal): # Gato hereda de Animal
    def especialidad(self):
        return "rasguña"

    def habla(self): # polimorfismo -sobreescribe un método de la clase Madre-
        return "miauuuu"

class Perro(Animal):
    def vicio(self):
        return "ladrar"

    # def habla(self):
    #     return "guauuuu"

g = Gato()
g.setNombre("Tom")
print(g.nombre)
print(g.especialidad())
print(g.habla())
p = Perro()
p.setNombre("Sansón")
print(p.nombre)
print(p.vicio())
print(p.habla())