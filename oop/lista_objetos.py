class Auto:
    def ponerMarca(self, m):
        self.marca = m

    def obtenerMarca(self):
        return self.marca

listaAutos = []
for i in range(3):
    a = Auto()
    marca = input("Ingrese marca: ")   
    a.ponerMarca(marca)
    listaAutos.append(a)

for auto in listaAutos:
    print(auto.obtenerMarca())
