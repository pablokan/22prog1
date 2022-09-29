# 14:50
# 15:09

from dataclasses import dataclass

@dataclass
class Remera:
    precioCompra: int
    precioVenta: int

class Negocio:
    def __init__(self) -> None:
        self.saldo = 30_000
        self.stock = 100
        self.remera = Remera(500, 1500)        

    def venta(self, cantidad):
        if cantidad > self.stock:
            print(f"\nLa cantidad requerida de {cantidad} remeras es superior al stock")
            print("Se realiza un descuento del 10% por el inconveniente")
            cantidadVendida = self.stock
            descuento = .9
        else:
            cantidadVendida = cantidad
            descuento = 1
        
        self.stock -= cantidadVendida
        montoVenta = cantidadVendida * self.remera.precioVenta * descuento
        self.saldo += montoVenta
        self.saldo = int(self.saldo)        
        print(f"Se vendieron {cantidadVendida} remeras por un total de {montoVenta} y la caja está en {self.saldo}.")

    def compra(self, cantidad):
        self.stock += cantidad        
        self.saldo -= (cantidad * self.remera.precioCompra)
        print(f"\nSe compraron {cantidad} remeras. El nuevo stock es {self.stock} y la caja está en {self.saldo}.")


n = Negocio()
n.venta(70)
n.compra(100)
n.venta(150)
n.compra(50)
