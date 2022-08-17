class Auto:
    def __init__(self, m): # método constructor
        # 1) se ejecuta automáticamente en el momento de la instanciación
        # 2) le envío los argumentos en la instanciación
        self.marca = m

    def obtenerMarca(self):
        return self.marca

listaAutos = []
for i in range(3):
    marca = input("Ingrese marca: ")   
    a = Auto(marca) # se activa el constructor
    listaAutos.append(a)

for auto in listaAutos:
    print(auto.obtenerMarca())
