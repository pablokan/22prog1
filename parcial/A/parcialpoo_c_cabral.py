from dataclasses import dataclass
from random import choice

@dataclass
class Remera:
    talle: str
    color = str(choice(("Blanco","Negro","Violeta","Marron")))
    precio: int = None

    def __post_init__(self):
        
        if self.talle == "s":
            self.precio = 500
        if self.talle == "m":
            self.precio = 600
        if self.talle == "l":
            self.precio = 700
        if self.talle == "xl":
            self.precio = 800

@dataclass
class Tienda:
    precio_venta = {"s":1500,"m":1800,"l":2100,"xl":2400}
    caja_actual: int = 30000
    stock = {"s":[Remera("s") for x in range(100)],"m":[Remera("m") for x in range(200)],"l":[Remera("l") for x in range(200)],"xl":[Remera("xl") for x in range(100)]}


    def comprar(self,cantCompra,talle):
        valor=self.stock[talle][0].precio
        if cantCompra*valor<=self.caja_actual:
            self.stock[talle]+=[Remera(talle) for i in range(cantCompra)]
            self.caja_actual-=valor*cantCompra
            print(f"Compra: {cantCompra} Remeras De Talle {talle}  Stock Actualizado: {len(self.stock[talle])} Talle {talle}  Caja: {self.caja_actual}")
        else:
            print(f"El Fondo Disponible Es ${self.caja_actual}, No Es Insuficiente Para Comprar {cantCompra} Remeras Talle {talle}.")
        
    def vender(self,cantVenta,talla):
            if cantVenta<=len(self.stock[talla]):
                del self.stock[talla][:cantVenta]
                self.caja_actual+=self.precio_venta[talla]*cantVenta
                print(f"Venta: {cantVenta} Remeras De Talle {talla}  Stock Actualizado: {len(self.stock[talla])}  Caja: {self.caja_actual}")
            else:
                print("No Hay Existencia Suficiente.")
                print(f"Se Anula La Operación De Venta De {cantVenta} Remeras De Talle {talla}")

    def estado_Fin(self):
        print(f"Estado Final.Caja: {self.caja_actual}")
        for i in self.precio_venta:
            for x in self.stock:
                print(f"Talle: {i} - Precio de Compra: {self.stock[x][0].precio} - Precio de Venta: {self.precio_venta[i]} - Stock: {len(self.stock[i])}")
                break


neg = Tienda()
neg.vender(100,'l')
neg.comprar(100,'s')
neg.vender(50,'m')
neg.comprar(100,'xl')
neg.vender(200,'m')
neg.comprar(50,'l')
neg.estado_Fin()
