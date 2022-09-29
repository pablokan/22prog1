from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio_compra: int
    precio_venta: int

@dataclass
class Empresa:
    nombre: str
    saldo: int
    stock: int

    def compra(self,producto,cantidad):
        valor = producto.precio_compra * cantidad
        self.stock += cantidad
        self.saldo = self.saldo - valor
        return f"\nSe efectuo una compra de {cantidad} {producto.nombre} al valor de {valor}. \nSu stock actual es de {self.stock} {producto.nombre} y su saldo actual es de {self.saldo} \n"
    
    def venta(self,producto,cantidad):
        if self.stock >= cantidad:
            valor = producto.precio_venta * cantidad
            self.stock = self.stock - cantidad
            self.saldo += valor
            return f"\nSe efectuo la venta de {cantidad} {producto.nombre} a valor de {valor}. \nSu stock actual es de {self.stock} {producto.nombre} y su saldo actual es de {self.saldo} \n"
        else:
            cantidad = self.stock
            valor = producto.precio_venta * cantidad
            valor = valor - (valor * 0.10)
            self.stock = 0
            self.saldo += valor
            return f"\nSTOCK INSUFICIENTE \nSe efectuo la venta de {cantidad} {producto.nombre} a valor de {valor}(10% de descuento por el inconveniente). \nSu stock actual es de {self.stock} {producto.nombre} (contacte con el proveedor) y su saldo actual es de {self.saldo} \n"

nombre = input("¿Cual es el nombre de su empresa?: ")
saldo = int(input("¿Con cuanto saldo inicia?: "))
stock = int(input("¿Cual es su stock inicial?: "))
empresa = Empresa(nombre,saldo,stock)
nombre = input("¿Que va a vender?: ")
compra = int(input("¿Cuanto vale el producto?: "))
venta = int(input("¿A cuanto piensa venderlo?: "))
producto = Producto(nombre,compra,venta)

print("Cuando quiera terminar la accion Comercial escriba 'Cierre'")
condicion = True
while condicion:
    print("¿Que desea hacer? \n(Respuestas esperadas: Compra   Venta    Cierre)")
    opcion = input("Respuesta: ").upper()
    if opcion == "COMPRA":
        cantidad = int(input("¿Cuanto desea comprar?: "))
        print(empresa.compra(producto,cantidad))
    elif opcion == "VENTA":
        cantidad = int(input("¿Cuanto desea vender?: "))
        print(empresa.venta(producto,cantidad))
    elif opcion == "CIERRE":
        condicion = False
    else:
        print("Su respuesta no coincide con ninguna de las mencionadas anteriormente. \nPruebe nuevamente: ")