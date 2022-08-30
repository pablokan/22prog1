from opsB import Suma

class Promedio(Suma):
    def promediar(self):
        self.resultado = self.resultado / 2

p1 = Promedio()
p1.pedirNumeros()
p1.operar()
p1.promediar()
p1.mostrarResultado()

