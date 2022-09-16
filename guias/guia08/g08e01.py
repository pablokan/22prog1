class Telefono:
    def ponerMarca(self, ma):
        self.marca = ma

    def ponerModelo(self, mo):
        self.modelo = mo

    def ponerCostoMensual(self, co):
        self.costoMensual = co

    def obtenerCostoAnual(self):
        return self.costoMensual * 12


t1 = Telefono()
t1.ponerMarca("HUawei")
t1.ponerModelo("No sé")
t1.ponerCostoMensual(1200)
print(t1.obtenerCostoAnual())