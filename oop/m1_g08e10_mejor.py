from m1_ope_mejor import Suma

class Promedio(Suma):
    def __init__(self, *args):
        super().__init__(*args)

    def promediar(self):
        self.resultado = self.resultado / self.cantidad

p1 = Promedio(2, 3)
p1.operar() # Suma
p1.promediar() # Promedio
print(p1.mostrarResultado()) # Operacion

