"""
compra $500 
venta $1500 
por unidad.

Si se quiere vender más de lo que hay en el stock, mostrar mensaje del faltante pero 
igualmente vender toda la existencia haciendo el 10% de descuento por el inconveniente.

Saldo de Caja inicial: $30000. Stock inicial: 100 remeras

Se realizan las siguientes operaciones en este orden estricto. 
Para cada operación, mostrar la cantidad de remeras, el monto y el saldo actualizado.

Vender 70
Comprar 100 
Vender 150
Comprar 50
Mostrar stock y saldo de caja"""




class Remera:
    def __init__(self,precio_compra,precio_venta):
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        

class Negocio:
    def __init__(self, stock, saldo):
        self.stock = stock
        self.saldo = saldo
        self.articulo = Remera(500,1500)

    def Comprar(self,cantidad):
        self.stock = self.stock + cantidad
        self.saldo -= cantidad * self.articulo.precio_compra
        print(f"Se compraron {cantidad} remeras. El nuevo stock es {self.stock} y la caja esta en ${int(self.saldo)}")
    
    def Vender(self,cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            ganancia = cantidad * self.articulo.precio_venta
            venta = cantidad
            
        else:
            print(f"La cantidad requerida de {cantidad} remeras es superior al stock.")
            print("Se realiza un descuento del %10 por el inconveniente")
            ganancia = self.stock * 1500 * 0.9
            venta = self.stock
            self.stock = 0
        
        self.saldo += ganancia
            
        print(f"Se vendieron {venta} remeras por un total {int(ganancia)} y la caja esta en {int(self.saldo)}")

    def Mostrar(self):
        print(f"El stock actual es: {int(self.stock)}")
        print(f"La caja esta en: ${int(self.saldo)}")

stock = 100
saldo = 30000
n = Negocio(stock,saldo)
n.Vender(70)
n.Comprar(100)
n.Vender(150)
n.Comprar(50)
n.Mostrar()



