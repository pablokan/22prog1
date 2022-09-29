"""
class Empresa():
    def __init__ (self):
        self.stock = 100
        self.saldo= 30_000
    def mostrarTotales(self):
        return self.saldo ,  self.stock

class Vender():
    def __init__(self, cV) -> None:
        self.cantidadVender = cV
        self.empresa= Empresa()
    def venta(self):
        if self.empresa.stock >= self.cantidadVender:
            self.totalVenta = self.cantidadVender * 1_500
            self.empresa.saldo+= self.empresa.saldo + self.totalVenta
            self.empresa.stock+= self.empresa.stock - self.cantidadVender
            return f" Se vendieron: {self.cantidadVender} por un total de {self.totalVenta} y la caja esta en {self.empresa.saldo} "
            
        else:
            self.empresa.saldo = self.empresa.saldo + (self.empresa.stock * 1350)
            print(f"La cantidad requerida de {self.cantidadVender} remeras es superior al stock.")
            print(f"Se realizara un descuento del 10% por el inconveniente.")
            return f"Se vendieron {self.empresa.stock} por un total de {self.empresa.stock * 1350} y la caja esta en {self.empresa.saldo}"

class Comprar():
    def __init__(self, cantidadComprar):
        self.cantidadComprar = cantidadComprar
        self.empresa= Empresa()

    def compra(self):
        self.empresa.saldo = self.empresa.saldo - (self.cantidadComprar * 500)
        self.empresa.stock = self.empresa.stock + self.cantidadComprar
        return f"se compraron {self.cantidadComprar} remeras. El nuevo stock es de {self.empresa.stock} y la caja esta en {self.empresa.saldo}"



venta1= Vender(140)
print(venta1.venta())
venta2=  Vender(20)
print(venta2.venta())
"""




class Remera:
    def __init__(self, precioVenta, precioCompra) -> None:
        self.precioVenta = precioVenta
        self.precioCompra = precioCompra    

class Negocio:
    def __init__(self):
        self.stock = 100
        self.saldo= 30_000
        self.precioCompra = Remera(1500, 500).precioCompra
        self.precioVenta = Remera(1500, 500).precioCompra
    
    def vender(self, cantidadVender):
        self.cantidadVender = cantidadVender
        if self.stock >= self.cantidadVender:
            self.totalVenta = self.cantidadVender * 1_500
            self.saldo= self.saldo + self.totalVenta
            self.stock= self.stock - self.cantidadVender
            print(f" Se vendieron: {self.cantidadVender} por un total de {self.totalVenta} y la caja esta en {self.saldo} ")
            
        else:
            self.saldo = self.saldo + (self.stock * 1350)
            print(f"La cantidad requerida de {self.cantidadVender} remeras es superior al stock.")
            print(f"Se realizara un descuento del 10% por el inconveniente.")
            print( f"Se vendieron {self.stock} por un total de {self.stock * 1350} y la caja esta en {self.saldo}")

    def comprar(self, cantidadComprar):
        self.cantidadComprar = cantidadComprar
        self.saldo = self.saldo - (self.cantidadComprar * 500)
        self.stock = self.stock + self.cantidadComprar
        print(f"se compraron {self.cantidadComprar} remeras. El nuevo stock es de {self.stock} y la caja esta en {self.saldo}")

    def mostrarTodo(self):
        print(f"Stock Final: {self.stock}. Saldo de caja: {self.saldo}")

remerulis= Negocio()
remerulis.vender(70)
remerulis.comprar(100)
remerulis.vender(150)
remerulis.comprar(50)
remerulis.mostrarTodo()

