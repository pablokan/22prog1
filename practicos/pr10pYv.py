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

    def adulto(self):
        if self.edad > 5:
            return True
        else:
            return False

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
            if tipoAnimal == "Pumas":
                caracP = [(230, 6), (180, 4), (210, 7), (190, 10)]
                a = Puma(i+1, *caracP[i])
            elif tipoAnimal == "Venados":
                caracV = [100, 130]
                a = Venado(i+1, caracV[i])
        
            self.listaAnimales.append(a)

    def getData(self) -> str:
        c = 0
        print(f"\nJaula de {self.tipoAnimal}")
        for animal in self.listaAnimales:
            print(f"# {animal.id} - {animal.salud()}")
            
    def getCantidadPumasAdultos(self):
        c = 0
        for puma in self.listaAnimales:
            if puma.adulto(): 
                    c += 1
        print(f"Cantidad de adultos: {c}")

jaulaPumas1 = Jaula("Pumas", 4)
jaulaPumas1.getData()
jaulaPumas1.getCantidadPumasAdultos()

jaulaVenados1 = Jaula("Venados", 2)
jaulaVenados1.getData()

# Salida
# Jaula de Pumas
# 1 - sano
# 2 - enfermo
# 3 - sano
# 4 - enfermo
# Cantidad de adultos: 3

# Jaula de Venados
# 1 - enfermo
# 2 - sano


