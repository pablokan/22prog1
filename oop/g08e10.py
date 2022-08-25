from inputs import inputNumber
from opera_validado import Suma

class Promedio(Suma):
    def promediar(self):
        self.resultado = self.resultado / 2

p1 = Promedio()
p1.pedirNumeros() # viene de Operacion
p1.operar() # viene de Suma
p1.promediar()
p1.mostrarResultado()
