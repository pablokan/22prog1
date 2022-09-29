stock = [
    {"talle": "S", "precioCompra": 500, "precioVenta": 1500, "cantidad": 100},
    {"talle": "M", "precioCompra": 600, "precioVenta": 1800, "cantidad": 200},
    {"talle": "L", "precioCompra": 700, "precioVenta": 2100, "cantidad": 200},
    {"talle": "XL", "precioCompra": 800, "precioVenta": 2400, "cantidad": 100},
]

class Remera:
    def __init__(self, t, c):
        self.talle = t
        self.cantidad = c

    def get_talle_cantidad(self):
        return f"{self.talle}, {self.cantidad}"

class Lista:
    def __init__(self):
        self.lista_remeras = []

    def agregar_lista(self):
        for datos in self.stock:
            talle, _, _, cantidad = datos.split(",")
            remera = Remera(talle, cantidad)
            self.lista_remeras.append(remera)

    def get_lista(self):
        for remera in self.lista_remeras:
            print(f"{remera.get_talle_cantidad}")

lista = Lista()
lista.agregar_lista()
lista.get_lista()
