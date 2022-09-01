class Auto():
    def __init__(self, ma,mo, an) -> None:
        self.marca = ma
        self.modelo = mo
        self.anio = an

class TuAuto(Auto):
    def __init__(self, ma, mo, an, du, co) -> None:
        super().__init__(ma, mo, an)
        self.duenio = du
        self.color = co

    def getColor(self):
        return self.color

    def __str__(self) -> str:
        return f"{self.duenio} {self.modelo}"

listaAutos = []
for i in range(3):
    # inputs
    # objeto = TuAuto(marca, modelo, etc)
    # listaAutos.append(objeto)
    pass

a = TuAuto("Fiat", "Duna", 1988, "Silvana", "rojo")
b = TuAuto("Ford", "Eco", 2016, "Pablo", "rojo")
c = TuAuto("VW", "Gol", 1999, "Toto", "gris")
listaAutos.append(a)
listaAutos.append(b)
listaAutos.append(c)

c = input("Ingrese color: ")
for auto in listaAutos:
    if auto.color == c:
        #print(auto.duenio)
        print(auto)
