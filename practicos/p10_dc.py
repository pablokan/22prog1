from dataclasses import dataclass

@dataclass
class Animal:
    id: int
    peso: float
        
    def salud(self):
        pass

@dataclass
class Puma(Animal):
    edad: int
    nombre: str = "Pumas"
    pesoSano: int = 200
    
    def __post_init__(self):
        print("__post_init__")
        self.data = [(230, 6), (180, 4), (210, 7), (190, 10)]

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
    pesoSano = 120
    def __init__(self, id, peso):
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
        pYe = [(230, 6), (180, 4), (210, 7), (190, 10)]
        pesos = [100, 130]
        for i in range(cantidadEjemplares):
            if tipoAnimal == "pumas":
                # peso = int(input("Peso: "))
                # edad = int(input("Edad: "))
                a = Puma(i+1, pYe[i][0], pYe[i][1]) # composición
            elif tipoAnimal == "venados":
                a = Venado(i+1, pesos[i])
            else:
                a = None

            self.listaAnimales.append(a)

    def getDatos(self):
        print(f"\nJaula de {self.tipoAnimal}")
        for puma in self.listaAnimales:
            print(f"# {puma.id} - {puma.salud()}")

    def cantidadAdultos(self):
        c = 0
        for puma in self.listaAnimales:
            if puma.adulto():
                c += 1
        print(f"La cantidad de adultos es {c}")


jaulaPumas1 = Jaula("pumas", 4)
jaulaPumas1.getDatos()
jaulaPumas1.cantidadAdultos()

jaulaVenados1 = Jaula("venados", 2)
jaulaVenados1.getDatos()
