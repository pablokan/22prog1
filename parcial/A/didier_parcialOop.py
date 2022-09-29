stockInicial = [
{"talle": "S", "precioCompra": 500, "precioVenta": 1500, "cantidad": 100},
{"talle": "M", "precioCompra": 600, "precioVenta": 1800, "cantidad": 200},
{"talle": "L", "precioCompra": 700, "precioVenta": 2100, "cantidad": 200},
{"talle": "XL", "precioCompra": 800, "precioVenta": 2400, "cantidad": 100}
]

from dataclasses import dataclass

@dataclass
class Remera:
    talle: str
    precioCompra = 0

    def __post_init__(self):
        if self.talle.upper() == "S":
            self.precioCompra = 500
        elif "M":
            self.precioCompra = 600
        elif "L":
            self.precioCompra = 700
        elif "XL":
            self.precioCompra = 800

@dataclass
class Remeralandia:
    caja: int = 30000
    precioVenta = {"S":1500,"M":1800,"L":2100,"XL":2400}
    stock = {
        "S":[Remera("S") for s in range(100)],
        "M":[Remera("M") for m in range(200)],
        "L":[Remera("L") for l in range(200)],
        "XL":[Remera('xl') for xl in range(100)]
        }
    


    def comprar(self,cantidadCompra,talle): 
        valor = self.stock[talle][0].precioCompra
        if cantidadCompra * valor <= self.caja:
            self.stock[talle] += [Remera(talle) for i in range(cantidadCompra)]
            self.caja -= (valor*cantidadCompra)
            print(f"Compra: {cantidadCompra} remeras de talle {talle} | Stock actualizado: {len(self.stock[talle])} talle {talle} | Caja: {self.caja}\n")
        else:
            print(f'El fondo disponible es ${self.caja}, no es insuficiente para comprar {cantidadCompra} remeras talle {talle}.\n')
        
    def vender(self,cantidadVenta,talle):
            if cantidadVenta <= len(self.stock[talle]):
                del self.stock[talle][:cantidadVenta]
                self.caja += (self.precioVenta[talle]*cantidadVenta)
                print(f"Venta: {cantidadVenta} remeras de talle {talle} | Stock actualizado: {len(self.stock[talle])} | Caja: {self.caja}\n")
            else:
                print("No hay existencia suficiente.")
                print(f"Se anula la operación de venta de {cantidadVenta} remeras de talle {talle}\n")
    def estado(self):
        print(f"Estado Final. Caja: {self.caja}")
        for a,b in zip(self.stock,self.precioVenta):
            print(f"Talle: {b} - Precio de Compra: {self.stock[a][0].precioCompra} - Precio de Venta: {self.precioVenta[b]} - Stock: {len(self.stock[b])}\n")



negocio = Remeralandia()
negocio.vender(100,"L")
negocio.comprar(100,"S")
negocio.vender(50,"M")
negocio.comprar(100,"XL")
negocio.vender(200,"M")
negocio.comprar(50,"L")
negocio.estado()