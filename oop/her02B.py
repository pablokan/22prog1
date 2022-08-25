class Animal:
    def __init__(self, n):
        self.nombre = n

    def habla(self):
        return "no sé que decir"

class Gato(Animal): # Gato hereda de Animal
    def __init__(self, n, e=99): # como mínimo los mismos parámetros que el constructor de la clase madre
        super().__init__(n) # llamada del constructor de la clase Madre
        self.edad = e

    def habla(self): # polimorfismo -sobreescribe un método de la clase Madre-
        return "miauuuu"

g = Gato("Tom", 5)
g2 = Gato("michina")
print(g.nombre, g.edad)
print(g.habla())
