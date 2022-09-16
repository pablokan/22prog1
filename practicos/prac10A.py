class Animal:
    def __init__(self, id, peso) -> None:
        self.id = id
        self.peso = peso

    def salud(self):
        pass

class Puma(Animal):
    def __init__(self, id, peso, edad):
        super().__init__(id, peso)
        self.edad = edad

    def salud(self):
        return "sano" if self.peso > 200 else "enfermo"

    def adulto(self):
        return True if self.edad > 5 else False


class Venado(Animal):
    def __init__(self, id, peso):
        super().__init__(id, peso)

    def salud(self):
        return "sano" if self.peso > 120 else "enfermo"

class Jaula: # compuesta de Animales
    def __init__(self, tipoAnimal, cantidadEjemplares):
        self.listaAnimales = []
        self.tipoAnimal = tipoAnimal

        for i in range(cantidadEjemplares):
            if tipoAnimal == "pumas":
                # peso = input("Peso: ")
                # edad = int(input("Edad: "))
                pYe = [(230, 6), (180, 4), (210, 7), (190, 10)]
                a = Puma(i+1, pYe[i][0], pYe[i][1])
            elif tipoAnimal == "venados":
                pYe = [100, 130]
                a = Venado(i+1, pYe[i])
            self.listaAnimales.append(a)

    def getDatos(self):
        print(f"\nJaula de {self.tipoAnimal}")
        for animal in self.listaAnimales:
            print(f"#{animal.id} - {animal.salud()}")

    def cantidadAdultos(self):
        c = 0
        for animal in self.listaAnimales:
            if animal.adulto():
                c += 1
        print(f"La cantidad de pumas adultos es {c}")

jaulaPumas1 = Jaula("pumas", 4)
jaulaPumas1.getDatos()
jaulaPumas1.cantidadAdultos()

jaulaVenados1 = Jaula("venados", 2)
jaulaVenados1.getDatos()
