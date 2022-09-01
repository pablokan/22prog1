from datetime import date

class Auto():
    def __init__(self, ma, an) -> None:
        self.marca = ma
        self.anio = an

    def antiguedad(self):
        anio = date.today().year
        return anio - self.anio

    def __str__(self) -> str:
        return f"{self.marca} {self.anio}"

a1 = Auto("VW", 2020)
a2 = Auto("Ford", 2010)
lista = [a1, a2]

for auto in lista:
    if auto.antiguedad() > 5:
        print(auto)
