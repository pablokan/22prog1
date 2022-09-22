class Auto:
    def ponerMarca(self, m):
        self.marca = m

    def ponerAnio(self, a):
        self.anio = a

    def obtenerMarca(self):
        return self.marca


a1 = Auto()
a2 = Auto()

a1.ponerMarca("VW")
a2.ponerMarca("Ford")

print(a1.marca)
print(a2.obtenerMarca())
