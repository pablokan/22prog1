from inputs import inputNumber

class Operacion: # clase abstracta:
    # es solo para ser heredada NO instanciada
    def pedirNumeros(self):
        self.n1 = inputNumber(int, "Ingrese primer número")
        self.n2 = inputNumber(int, "Ingrese segundo número")

    def operar(self): # método abstracto
        pass

    def mostrarResultado(self):
        print(self.resultado)

class Suma(Operacion):
    def operar(self): # polimorfismo
        self.resultado = self.n1 + self.n2

class Resta(Operacion):
    def operar(self):
        self.resultado = self.n1 - self.n2

if __name__ == "__main__":
    s1 = Suma()
    s1.pedirNumeros()
    s1.operar()
    s1.mostrarResultado()

    r1 = Resta()
    r1.pedirNumeros()
    r1.operar()
    r1.mostrarResultado()
