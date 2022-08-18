class Auto:
    def __init__(self, m, a):
        self.marca = m
        self.anio = a
    
    def mostrarMarca(self):
        return self.marca

    def __str__(self) -> str:
        return f"Este auto es un {self.marca} del año {self.anio}"

listaAutos = []

for i in range(3):
    marca = input("Ingrese marca: ")
    anio = input("Ingrese año: ")
    auto = Auto(marca, anio)
    listaAutos.append(auto)

for i in range(3):
    print(listaAutos[i].marca)

for auto in listaAutos:
    print(auto)
