from m1_operaciones import Suma

class Promedio(Suma):
    def promediar(self):
        self.resultado = self.resultado / 2

p1 = Promedio()
p1.pedirNumeros() # Operacion
p1.operar() # Suma
p1.promediar() # Promedio
p1.mostrarResultado() # Operacion

