from dataclasses import dataclass
@dataclass
class Ventaremeras:
    saldoinicial=30000
    stockinicial=100
    preciocompra=500
    precioventa=1500
    def __init__(self):
        print(f"stok inicial:{self.stockinicial} \n saldo inicial:{self.saldoinicial}")
    def venta(self,cv):
        self.cantidadventa = cv
        valor=self.cantidadventa*self.precioventa
        if self.cantidadventa > self.stockinicial:
            valorcd=(self.stockinicial*self.precioventa)-0.10
            self.stockinicial = 0
            return(f"La cantidad requerida de {self.cantidadventa} remeras es superior al stock."'\n'
            "Se realiza un descuento del 10% por el inconveniente."'\n'
            f"Se vendieron {self.stockinicial}por un total de {valorcd}y la caja esta en{self.saldoinicial+valorcd}")
            
        else: 
            return(f"Se vendieron {self.cantidadventa}por un total de {valor}y la caja esta en{self.saldoinicial}")   
   
    def compra(self,cc):
        self.cantidadcompra = cc
        self.stockinicial=self.stockinicial+self.cantidadcompra
        compras=self.saldoinicial-(self.cantidadcompra*self.preciocompra)
        if compras>self.saldoinicial:
           return(f"te quedaste sin dinero con la compra de {self.cantidadcompra} remeras")
        else:
            return(f"Se compraron {self.cantidadcompra} remeras. El nuevo stock es {self.stockinicial} y la caja está en {compras}")


cantventa=int(input("cuantas remeras se vendieron: "))
cantcompra=int(input("cuantas remeras se compraron: "))
print(Ventaremeras.venta(cantventa))
print(Ventaremeras.compra(cantcompra))