#RemeraLandia Parcial Julieta Bulfon
stock = [
    {"talle": "S", "precioCompra": 500, "precioVenta": 1500, "cantidad": 100},
    {"talle": "M", "precioCompra": 600, "precioVenta": 1800, "cantidad": 200},
    {"talle": "L", "precioCompra": 700, "precioVenta": 2100, "cantidad": 200},
    {"talle": "XL", "precioCompra": 800, "precioVenta": 2400, "cantidad": 100},
]

# 4 objetos de una sola clase

from dataclasses import dataclass

@dataclass

class Remeras:
    def __init__(self) -> None:
        self.listaTalleS = [500, 1500, 100]
        self.listaTalleM = [600, 1800, 200]
        self.listaTalleL = [700, 2100, 200]
        self.listaTalleXL = [800, 2400, 100]
        self.cajaInicio: int = 30000
    
    def ventaL(self, cantidad, stockL) -> None: #Venta y actualizacion Talle L
        self.cantidad = int(input("Ingrese la cantidad de remeras talle L que quiere comprar: "))
        self.totalVenta = self.cantidad * (self.listaTalleL [1])
        self.stockL = (self.listaTalleL[2])
        self.stockAct = self.stockL - self.cantidad
        self.cajaAct = self.cajaInicio + self.totalVenta
        print(f"Venta:{cantidad} remeras de talle L. Stock actualizado: {self.stockAct}. Caja: {self.cajaAct}")

    def compraS(self, cantidad, stockS) -> None: #Venta y actualización Talle S
        self.cantidad = int(input("Ingrese la cantidad de remeras talle S que quiere comprar: "))
        self.totalCompra = self.cantidad * (self.listaTalleS[0])
        self.stockS = (self.listaTalleS[2])
        self.stockAct = self.stockS + self.cantidad
        self.cajaAct = self.cajaInicio - self.totalCompra
        print(f"Compra:{cantidad} remeras de talle S. Stock actualizado: {self.stockAct}. Caja: {self.cajaAct}")
    
    def ventaM(self, cantidad, stockM) -> None: #Venta y actualización talle M
        self.cantidad = int(input("Ingrese la cantidad de remeras talle M que quiere vender: "))
        self.totalVenta = self.cantidad *(self.listaTalleM[1])
        self.stockM = (self.listaTalleM[2])
        self.stockAct = self.stockM - self.cantidad
        self.cajaAct = self.cajaInicio + self.totalVenta
        print(f"Venta:{cantidad} remeras de talle M. Stock actualizado: {self.stockAct}. Caja: {self.cajaAct}")
    
    def compraXL(self, cantidad, stockXL) -> None: #Venta y actualización talle XL
        self.cantidad = int(input("Ingrese la cantidad de remeras talle XL que quiere comprar: "))
        self.totalCompra = self.cantidad * (self.listaTalleXL[0])
        self.stockXL = (self.listaTalleXL[2])
        self.stockAct = self.stockS + self.cantidad
        self.cajaAct = self.cajaInicio - self.totalCompra
        print(f"Compra:{cantidad} remeras de talle XL. Stock actualizado: {self.stockAct}. Caja: {self.cajaAct}")
    
    def ventaNot(self,cantidad,stock): # metodo para venta imposible
        self.cantidad = int(input("Ingrese la cantidad de remeras talle M que quiere comprar: "))
        self.stockM = (self.listaTalleM[2])
        if self.cantidad < self.stockM:
               print(f"No hay existencia suficiente. Se anula la operación de venta.")
        else:
               print(f"Venta:{cantidad} remeras de talle M. Stock actualizado: {self.stockAct}. Caja: {self.cajaAct}")
        
    def ventaL(self, cantidad, stockL) -> None: #Venta y actualizacion Talle L
        self.cantidad = int(input("Ingrese la cantidad de remeras talle L que quiere comprar: "))
        self.totalVenta = self.cantidad * (self.listaTalleL [1])
        self.stockL = (self.listaTalleL[2])
        self.stockAct = self.stockL - self.cantidad
        self.cajaAct = self.cajaInicio + self.totalVenta
        print(f"Venta:{cantidad} remeras de talle L. Stock actualizado: {self.stockAct}. Caja: {self.cajaAct}")

if __name__ == "__main__":
    textil1 = Remeras()
    textil1.ventaL(100,200)
    textil1.compraS(100,100)
    textil1.ventaM(50,200)
    textil1.compraXL(100,200)
    textil1.ventaNot(200, 200)
    textil1.ventaL(100, 200)




    

        