import os
from dataclasses import dataclass, asdict

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
        self.lRd = [asdict(o) for o in self.listaRemeras]
        self.lDs = [{d["talle"]: [d["cantidad"], d["precioCompra"], d["precioVenta"]]} for d in self.lRd]
        print(self.lDs)

    def compra(self, cantidad, talle):
        print(f"\nCompra: {cantidad} remeras de talle {talle}", end=" | ")
        self.lDs[talle][0] += cantidad
        print(f"Stock actualizado: {self.lDs[talle]}", end=" | ")
        self.caja -= self.lDs[talle][1] * cantidad
        print(f"Caja: {self.caja}")

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
negocio.compra(100, "S")
negocio.getAll("Final")
