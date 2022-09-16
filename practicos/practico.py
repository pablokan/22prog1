
class Animal:

    def __init__(self,i,p):
        self.id = i
        self.peso = p

    def estaSano(self,p): 
        if self.peso >= p:
            return "está sano"
        else:
            return "está enfermo"     

class Puma(Animal):
    adulto = False

    def __init__(self, i, p,e):
        super().__init__(i, p)
        self.edad = e

    def estaSano(self):
        if self.peso >= 200:
            return "está sano"
        else:
            return "está enfermo"

    def esAdulto(self): 
        if self.edad > 5:
            adulto = True
        else:
            adulto = False
        return adulto

class Venado(Animal):
    def __init__(self, i, p):
        super().__init__(i, p)

    def estaSano(self):
        if self.peso >= 120:
            return "está sano"
        else:
            return "está enfermo"

class Jaula:
    pumas = []
    venados = []

    def __init__(self,tA,c):
        self.cantidad = c
        self.tipoAnimal = tA
        if self.tipoAnimal.lower() == "puma":
            print(f"Usted va a insertar {self.cantidad} ejemplares del animal: {self.tipoAnimal}")
            for i in range(self.cantidad):
                peso = int(input("Inserte el peso del puma Nº " + str(i+1) +": "))
                edad = int(input("Inserte la edad del puma Nº " + str(i+1) +": "))
                self.pumas.append(Puma(i + 1,peso,edad))
        elif self.tipoAnimal.lower() == "venado":
            print(f"Usted va a insertar {self.cantidad} ejemplares del animal: {self.tipoAnimal}")
            for i in range(self.cantidad):
                peso = int(input("Inserte el peso del venado Nº " + str(i+1) + ": "))
                self.venados.append(Venado(i + 1,peso))

    def getSaludVenados(self):
        for venado in self.venados:
            print(f"El venado de ID {venado.id} {venado.estaSano()} ")

    def getSaludPumas(self):
        for puma in self.pumas:
            print(f"El puma de ID {puma.id} {puma.estaSano()} ")

    def getAdultos(self):
        adultos = 0
        for animal in self.pumas:
            if animal.esAdulto():
                adultos += 1
        print(f"Hay {adultos} pumas adultos.")
           


jaulaPumas = Jaula("Puma",4)
jaulaPumas.getSaludPumas()
jaulaPumas.getAdultos()

jaulaVenados = Jaula("Venado", 2)
jaulaVenados.getSaludVenados()