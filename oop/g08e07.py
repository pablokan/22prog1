#Heredar de la clase Auto una clase Marca, que agregue el atributo Modelo. Instanciar en  el programa principal (una sola línea en total). La salida debe ser por ejemplo: Auto: VW Modelo: Gol

class Auto:
    def __init__(self, marca):
        self.marca = marca

class Marca(Auto):
    def __init__(self, marca, modelo):
        Auto.__init__(self, marca)
        self.modelo = modelo
        print(f"Auto: {self.marca}")
        print(f"Modelo: {self.modelo}")

a = Marca("VW", "Gol")