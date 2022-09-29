import os
from dataclasses import dataclass

@dataclass
class Remera:
    talle: str
    precioCompra: float
    precioVenta: float
    cantidad: int

@dataclass
class Negocio:
    nombre: str
    stock: list[dict]
    caja: int = 30_000

    def __post_init__(self):
        self.listaRemeras = [Remera(**t) for t in stock]

    def compra(self, cantidad, talle):
        print(f"\nCompra: {cantidad} remeras de talle {talle}", end=" | ")
        for remera in self.listaRemeras:
            if remera.talle == talle:
                remera.cantidad += cantidad
                print(f"Stock actualizado: {remera.cantidad}", end=" | ")
                self.caja -= remera.precioCompra * cantidad
        print(f"Caja: {self.caja}")

    def venta(self, cantidad, talle):
        for remera in self.listaRemeras:
            if remera.talle == talle:
                if remera.cantidad >= cantidad:
                    print(f"\nVenta: {cantidad} remeras de talle {talle}", end=" | ")
                    remera.cantidad -= cantidad
                    print(f"Stock actualizado: {remera.cantidad}", end=" | ")
                    self.caja += remera.precioVenta * cantidad
                    print(f"Caja: {self.caja}")
                else:
                    print(f"\nNo hay existencia suficiente. Se anula la operación de venta de {cantidad} remeras de talle {talle}")
        


    def getAll(self, estado):
        print(f"\nEstado {estado}. Caja: {self.caja}")
        for t in self.listaRemeras:
            print(t)


stock = [
    {"talle": "S", "precioCompra": 500, "precioVenta": 1500, "cantidad": 100},
    {"talle": "M", "precioCompra": 600, "precioVenta": 1800, "cantidad": 200},
    {"talle": "L", "precioCompra": 700, "precioVenta": 2100, "cantidad": 200},
    {"talle": "XL", "precioCompra": 800, "precioVenta": 2400, "cantidad": 100},
]

os.system("clear")
negocio = Negocio("Remeralandia", stock)

negocio.getAll("Inicial")

negocio.venta(100, "L")
negocio.compra(100, "S")
negocio.venta(50, "M")
negocio.compra(100, "XL")
negocio.venta(200, "M")
negocio.compra(50, "L")

negocio.getAll("Final")
