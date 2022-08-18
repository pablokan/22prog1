# Definir una clase que al ser instanciada reciba un valor numérico y cargue una lista de nombres hasta esa cantidad. Hacer también un método que muestre la lista completa.

class ValorNumerico():
    def __init__(self, cantidad) -> None:
        self.lista = []
        for x in range(cantidad):
            nombre = input("Nombre: ")
            self.lista.append(nombre)

    def mostrarLista(self):
        print(self.lista)

grupo1 = ValorNumerico(3)
grupo1.mostrarLista()
