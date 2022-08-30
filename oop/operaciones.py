from inputs import inputNumber

class Operacion: # clase abstracta: solamente sirve para ser heredada, no se puede instanciar
    def pedirNumeros(self):
        self.n1 = inputNumber(int, 'Ingrese primer número: ')
        self.n2 = inputNumber(int, 'Ingrese segundo número: ')

    def operar(self): # método abstracto
        pass

    def mostrarResultado(self):
        print(self.resultado)

class Suma(Operacion): # Operacion SOLO acá
    def operar(self): # polimorfismo, sobreescribir el método de la clase madre
        self.resultado = self.n1 + self.n2

class Resta(Operacion):
    def operar(self):
        self.resultado = self.n1 - self.n2

s1 = Suma()
s1.pedirNumeros()
s1.operar()
s1.mostrarResultado()

r1 = Resta()
r1.pedirNumeros()
r1.operar()
r1.mostrarResultado()

o = Operacion() # esto NO se debe hacer, las clases abstractas NO deben ser instanciadas