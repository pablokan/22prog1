class Animal:
    def __init__(self, id, peso) -> None:
        self.id = id
        self.peso = peso
        
    def salud(self): # método abstracto
        pass

class Puma(Animal):
    pesoSano = 200
    especie = "Pumas"
    pYe = [(230, 6), (180, 4), (210, 7), (190, 10)]
    def __init__(self, id, peso, edad):
        super().__init__(id, peso)
        self.edad = edad

    def salud(self):
        if self.peso > self.pesoSano:
            return "sano"
        else:
            return "enfermo"


    def adulto(self):
        if self.edad > 5:
            return True
        else:
            return False

class Venado(Animal):
    pYe = [(100, None), (130, None)]
    pesoSano = 120
    especie = "Venados"
    def __init__(self, id, peso, _):
        super().__init__(id, peso)
        
    def salud(self):
        if self.peso > self.pesoSano:
            return "sano"
        else:
            return "enfermo"


class Jaula: # Compuesta de pumas o venados
    def __init__(self, tipoAnimal, cantidadEjemplares):
        self.listaAnimales = []
        self.tipoAnimal = tipoAnimal
        
        for i in range(cantidadEjemplares):
            a = tipoAnimal(i+1, tipoAnimal.pYe[i][0], tipoAnimal.pYe[i][1]) # composición
            self.listaAnimales.append(a)

    def getDatos(self):
        print(f"\nJaula de {self.tipoAnimal.especie}")
        for puma in self.listaAnimales:
            print(f"# {puma.id} - {puma.salud()}")

    def cantidadAdultos(self):
        c = 0
        for puma in self.listaAnimales:
            if puma.adulto():
                c += 1
        print(f"La cantidad de adultos es {c}")


jaulaPumas1 = Jaula(Puma, 4)
jaulaPumas1.getDatos()
jaulaPumas1.cantidadAdultos()

jaulaVenados1 = Jaula(Venado, 2)
jaulaVenados1.getDatos()