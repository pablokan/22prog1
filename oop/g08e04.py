class Algo:
    def __init__(self, cantidad) -> None:
        self.lista = []
        for i in range(cantidad):
            nombre = input("Nombre: ")
            self.lista.append(nombre)

    def mostrarLista(self):
        for nombre in self.lista:
            print(nombre)

alguito = Algo(3)
alguito.mostrarLista()
