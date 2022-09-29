#IEOB filiberti
# remeralandia

class Remeralandia:
    pass
    def __init__(self,saldo,stock,cantidad,valorCompra,valorVenta,saldoInicial,StockInicial):
        self.saldo = saldo
        self.stock =stock
        self.cantidad=cantidad
        self.valorCompra=valorCompra 
        self.valorVenta=valorVenta
        self.saldoInicial=saldoInicial
        self.StockInicial=StockInicial 
    def ingresarDatos(self,saldo,stock,cantidad,valorCompra,valorVenta ):
        self.saldo= self.saldoInicial + (valorCompra * cantidad)
        self.stock=self.StockInicial + self.cantidad
        self.cantidad=[int(input("ingresar cantidad de remeras: "))for c in range (1)]


print (Remeralandia)
class OpBasicas(Remeralandia):
    def __init__(self,saldo,stock,cantidad,valorCompra,valorVenta):
            OpBasicas.__init__(self,saldo,stock,cantidad,valorCompra,valorVenta)
    

    def venta(self,saldo,stock,cantidad,valorVenta):
        total= (self.cantidad * self.valorVenta)
        caja= self.saldoInicial + total
        print("se vendieron",self.cantidad,"por un total de",total, "y la caja esta en", caja)

    def compra(self,saldo,stock,cantidad,valorVenta):
        total= (self.cantidad * self.valorCompra)
        caja= self.saldoInicial - total
        nuevoStock= self.StockInicial + cantidad
        print("se compraron",self.cantidad,"por un total de",total, "el nuevo stock es",nuevoStock,"y la caja esta en", caja)
    
remera= (OpBasicas(30000,100,70,1500,))

print=(remera)


