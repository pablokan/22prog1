from dataclasses import dataclass

@dataclass
class Remera:
    precioVenta: int
    precioCompra: int

@dataclass
class Negocio:
    nombre: str
    saldo: int
    stock: int

    def vender(self, remerasVender):

        if self.stock < remerasVender:
            venta = self.stock * 1500 - (self.stock * 10 / 100)
            self.saldo -= venta

            print(f"La cantidad requerida de {self.stock} remeras es superior al stock.")
            print(f"Se realiza un descuento del 10% por el inconveniente.")
            print(f"Se vendieron {remerasVender} remeras por un total de {venta} y la caja está en {self.saldo}")
        
        else:
            venta = remerasVender * 1500
            self.saldo += venta 
            print(f"Se vendieron {remerasVender} remeras por un total de {venta} y la caja está en {self.saldo}")
           
    def comprar(self, remerasComprar):
        compra = remerasComprar * 500
        self.saldo -= compra
        self.stock = self.stock + remerasComprar

        print(f"Se compraron {remerasComprar} El nuevo stock es {compra} y la caja está en {self.saldo}")
    

negocio = Remera(1500, 500)
negocio = Negocio("Remeralandia", 30000, 100)

negocio.vender(70)
negocio.comprar(100)
negocio.vender(150)
negocio.comprar(50)

