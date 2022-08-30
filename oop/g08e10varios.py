from ops_varios import Suma

class Promedio(Suma):
    def promediar(self):
        self.resultado = self.resultado / self.cantidad

p1 = Promedio(2,3,3)
p1.operar()
p1.promediar()
p1.mostrarResultado()

