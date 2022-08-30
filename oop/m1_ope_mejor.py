class Operacion:
    def __init__(self, *args):
        self.numeros = list(args)
        self.cantidad = len(args)

    def operar(self): # método abstracto
        pass

    def mostrarResultado(self):
        return self.resultado

class Suma(Operacion):
    def __init__(self, *args):
        super().__init__(*args)

    def operar(self): # polimorfismo
        self.resultado = sum(self.numeros)


if __name__ == "__main__":
    s1 = Suma(1, 2, 3, 4)
    s1.operar()    
    print(s1.mostrarResultado())

