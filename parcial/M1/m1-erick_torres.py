class Caja:
    def __init__(self, inicial, stock) -> None:
        self.inicial = inicial
        self.stock = stock
        self.remera = Remera(500, 1500)

    def comprar(self, cantidadComprada):
        if cantidadComprada > 0:
            self.stock += cantidadComprada
            self.inicial = self.inicial - (cantidadComprada * self.remera.precioCompra)
            return f'Se compraron {cantidadComprada} remeras. El nuevo stock es {self.stock} y la caja está en {self.inicial}.'
    
    def vender(self, cantidadVendida):
        if self.stock < cantidadVendida:
            stockViejo = self.stock
            total = stockViejo * self.remera.precioVenta
            total = total - (total / 10)            
            self.stock = 0
            self.inicial += total
            return f'La cantidad requerida de {cantidadVendida} es mayor al stock. \nSe realiza el descuento del 10% por el inconveniente. \nSe vendieron {stockViejo} remeras por un total de {total} y la caja esta en {self.inicial}.' 
        if cantidadVendida > 0 and cantidadVendida < self.stock:
            total = cantidadVendida * self.remera.precioVenta
            self.inicial += total
            self.stock = self.stock - cantidadVendida
            return f'Se vendieron {cantidadVendida} remeras por un total de {total} y la caja está en {self.inicial}.'
        else:
            return f'Cantidad de remeras debe ser mayor a 0'

    def hacerCaja(self):
        return f'Caja: {self.inicial} Stock: {self.stock}'

class Remera:
    def __init__(self, precioCompra, precioVenta) -> None:
        self.precioCompra = precioCompra
        self.precioVenta = precioVenta
    

#Vender 70
#Comprar 100 
#Vender 150
#Comprar 50
#Mostrar stock y saldo de caja

remeralandia = Caja(30000, 100)
print(remeralandia.vender(70))
print(remeralandia.comprar(100))
print(remeralandia.vender(150))
print(remeralandia.comprar(50))
print(remeralandia.hacerCaja())