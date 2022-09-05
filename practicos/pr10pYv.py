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
        if self.peso >= 200:
            return "sano"
        else:
            return "enfermo"

class Venado(Animal):
        def __init__(self, id, peso) -> None:
            super().__init__(id, peso)

        def salud(self):
            if self.peso >= 120:
                return "sano"
            else:
                return "enfermo"


class Jaula:
    def __init__(self, tipoAnimal, cantidad) -> None:
        self.listaAnimales = []
        self.tipoAnimal = tipoAnimal
        for i in range(cantidad):
            if tipoAnimal == "Puma":
                a = Puma(i+1, input("Peso: "), input("Edad: "))
            elif tipoAnimal == "Venado":
                a = Venado(i+1, input("Peso: "))
        
        self.listaAnimales.append(a)

    def getData(self) -> str:
        c = 0
        for animal in self.listaAnimales:
            print(f"# {animal.id} - {animal.salud()}")
            if animal.edad > 5 and self.tipoAnimal == "Puma":
                c += 1
        if c != 0:
            print(f"Cantidad de adultos: {c}")

jaulaPumas1 = Jaula("Puma", 3)
jaulaPumas1.getData()

jaulaVenados1 = Jaula("Venado", 2)
jaulaVenados1.getData()

        

