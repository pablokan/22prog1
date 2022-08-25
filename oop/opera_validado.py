from inputs import inputNumber

class Operacion: # clase abstracta (solamente existe para ser heredada, NO para ser instanciada)
    def pedirNumeros(self):
        self.n1 = inputNumber(int, "Ingrese primer operando: ")
        self.n2 = inputNumber(int, "Ingrese segundo operando: ")

    def operar(self): # método abstracto
        # las clases hijas redefinen las operaciones respectivas
        pass

    def mostrarResultado(self):
        print(self.resultado)

class Suma(Operacion):
    def operar(self): # polimorfismo
        # reescritura de un método con el mismo nombre en una clase hija
        self.resultado = self.n1 + self.n2

class Resta(Operacion):
    def operar(self): # polimorfismo
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

