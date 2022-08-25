class Operacion: # clase abstracta (solamente existe para ser heredada, NO para ser instanciada)
    def pedirNumeros(self):
        self.n1 = int(input("Ingrese primer operando: "))
        self.n2 = int(input("Ingrese segundo operando: "))

    def operar(self): # método abstracto
        # las clases hijas redefinen las operaciones respectivas
        pass

    def mostrarResultado(self):
        print(self.resultado)


class Suma(Operacion):
    def operar(self):
        self.resultado = self.n1 + self.n2

s1 = Suma()
s1.pedirNumeros()
s1.operar()
s1.mostrarResultado()

class Resta(Operacion):
    def operar(self):
        self.resultado = self.n1 - self.n2

r1 = Resta()
r1.pedirNumeros()
r1.operar()
r1.mostrarResultado()

