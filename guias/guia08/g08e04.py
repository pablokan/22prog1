class Algo:
    def __init__(self, cantidad) -> None:
        self.listaNombres = []
        for i in range(cantidad):
            nombre = input("Nombre: ")
            self.listaNombres.append(nombre)

    def mostrarLista(self):
        print(self.listaNombres)

a = Algo(3)
a.mostrarLista()