from inputs import inputNumber

class Operacion: # clase abstracta:
    # es solo para ser heredada NO instanciada
    def __init__(self, *args):
        self.numeros = list(args)
        self.cantidad = len(args)

    def operar(self): # método abstracto
        pass

    def mostrarResultado(self):
        print(self.resultado)

class Suma(Operacion):
    # def __init__(self, *args): esto lo hace igual
    #     super().__init__(*args)
    def operar(self): # polimorfismo
        self.resultado = sum(self.numeros)

if __name__ == "__main__":
    s1 = Suma(2,3,3)
    s1.operar()
    s1.mostrarResultado()
