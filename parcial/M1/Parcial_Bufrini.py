from dataclasses import dataclass

@dataclass
class Caja:
    compra: int 
    venta: int 
    saldo: int
    stock: int

@dataclass
class Pedido:
    
    def compra(self,remera,cantidad):
            precio = remera.compra * cantidad
            self.stock += cantidad
            self.saldo = self.saldo - precio
            return f"Se hizo una compra de {cantidad} remeras. Con un precio de {precio}.Stock actual: {self.stock} \n , saldo actual : {self.saldo}"

    def venta(self,cantidad):
        if self.stock > cantidad:
            precio = self.venta *cantidad
            self.stock -= cantidad
            self.saldo += precio
            return f"Se vendieron {cantidad} remeras.\n Stock: {self.stock} \n Saldo: {self.saldo}"
        else:
            cantidad = self.stock
            precio = self.venta * cantidad
            precio = precio - (precio * 0.10)
            self.saldo += precio
            return f"No hay stock por lo tanto se hará la venta de {self.cantidad} remeras con un descuento del 10%.\n Stock:{self.stock}\n Saldo:{self.saldo}"

compra = input("Cual es el precio de compra de las remeras? ")
venta = input("Cual es el precio de venta de las remeras? ")
saldo = input("Cual es el saldo inicial de la empresa? ")
stock = input("Cual es el stock inicial dde la empresa? ")
pedido = Pedido()

caja = Caja(compra,venta,saldo,stock)
cantidad = int(input("¿Cuantas remeras quiere comprar? "))


"""
Asi habia arrancado pero no podia setear los valores de una, por eso los pedi con un input, que tampoco me salio, pero bueno, se intento

from dataclasses import dataclass

@dataclass
class Caja:
    compra: int = 500
    venta: int = 1500
    saldo: int = 30_000
    stock: int = 100

    def setPrecios(self , c , v ):
        self.compra = c
        self.venta = v

    def setStock(self , s , k):
        self.saldo = s
        self.stock = k

@dataclass
class Pedidos(Caja):
    
    def venta(self):
        pedido = int(input("Ingrese la cantidad de remeras que quiere vender: "))
        
        self.saldo = pedido * self.venta
        self.stock += pedido
        if pedido > self.stock:
            pedido * self.venta / 0.10
            print(f"La cantidad requerida de {pedido}remeras es superior al stock. Se hace un descuento del 10%")

    def compra(self):
        pedido = int(input("Ingrese la cantidad de remeras que quiere comprar: "))
        monto_compra = pedido * self.compra
        self.saldo -= monto_compra
        self.stock -= pedido 

    def mostrarTodo(self):
        print(f"El stock es de: ",self.stock)
        print(f"El saldo actual de la caja es de: " ,self.saldo)

pedidos = Pedidos()
pedidos.venta()
pedidos.compra()
pedidos.mostrarTodo()"""