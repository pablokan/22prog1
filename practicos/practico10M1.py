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
        return "sano" if self.peso >= 200 else "enfermo"

    def adulto(self):
        return True if self.edad > 5 else False
        
         
class Venado(Animal):
    def __init__(self, id, peso) -> None:
        super().__init__(id, peso)

    def salud(self):
        return "sano" if self.peso >= 120 else "enfermo"

class Jaula: # compuesta por Pumas o Venados
    def __init__(self, tipoAnimal, cantidadEjemplares):
        self.listaAnimales = []
        print(f"\nJaula de {tipoAnimal}")
        for i in range(cantidadEjemplares):
            if tipoAnimal == "pumas":
                pesosYedades = [(230, 6), (180, 4), (210, 7), (190, 10)]
                peso, edad = pesosYedades[i]
                a = Puma(i+1, peso, edad)
            elif tipoAnimal == "venados":
                pesos = [100, 130]
                a = Venado(i+1, pesos[i])
            self.listaAnimales.append(a)

    def getData(self):
        for animal in self.listaAnimales:
            print(f"# {animal.id} - {animal.salud()} porque pesa: {animal.peso}")

    def cantidadAdultos(self):
        c = 0
        for animal in self.listaAnimales:
            if animal.adulto():
                c += 1
        return f"Cantidad de pumas adultos: {c}"

jaulaPumas01 = Jaula("pumas", 4)
jaulaPumas01.getData()
print(jaulaPumas01.cantidadAdultos())

jaulaVenados = Jaula("venados", 2)
jaulaVenados.getData()


