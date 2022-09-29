from dataclasses import dataclass
@dataclass
class Ropa:
    id:str
    tipo:str
    stock:int
    precio:int


class Negocio:
    def __init__(self) -> None:
        self.caja = 100000
        self.listRopa = []
        self.inventario = [["#1","jean", 30, 3000],
        ["#2","gabardina", 40, 4000],
        ["#3","remera lisa", 10, 1000],
        ["#4","remera estampada", 20, 2000]]
        for inventario in self.inventario:
            p = Ropa(*inventario)
            self.listRopa.append(p)  

    def venta(self,tipo,cantidad):
        for ropa in self.listRopa:
            if tipo == ropa.tipo :
                if ropa.stock >= cantidad:
                    venta = cantidad * ropa.precio
                    ropa.stock -= cantidad
                    self.caja += venta
                    print(f"venta:{cantidad} {tipo} |stock actualizado: {ropa.stock} |caja:{self.caja}")
                else: 
                    print( f"No hay existencia suficiente. Se anula la operación de venta de {cantidad} {tipo}")
    
    def mostrarDatos(self):
        for prenda in self.inventario:
            print(prenda)

n1 = Negocio()
n1.venta("jean",15)
n1.venta("remera lisa",10)
n1.venta("jean",20)
n1.venta("gabardina",20)
n1.mostrarDatos() 