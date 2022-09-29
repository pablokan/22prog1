from dataclasses import dataclass


@dataclass
class Remeras:
    talle: str = str ["S","M","L","XL"]
    precioCompra: float = float [500,600,700,800]
    precioVenta: float = float [1500,1800,2100,2400]
    cantidad: int = int [100,200,200,100]



class Negocio(Remeras):
    cajaActual: float = 300000
    #def __init__(self) -> None:
        #stock= [["S",500,1500,100],["M",600,1800,200],["L",700,2100,200],["XL",800,2400,100]]
    stock = 600

        """"self.listaTalles = []
        for talle in stock:
            t = Negocio(*talle)[0]
            self.listaTalles.append(t)"""
    def comprar(self, cantCompra,):
        if cantCompra*600 <= self.cajaActual:
            self.stock += [Remeras() for i in range(cantCompra)]
            self.cajaActual -= 600*cantCompra
            print(f"se compraron {cantCompra} remeras. El nuevo stock es {len(self.stock)} y la caja está en ${self.cajaActual}")
        else:
            print(f"El fondo disponible ${self.cajaActual}, no es suficiente para comprar {cantCompra} se cancela la compra.\n")
    def vender(self, cantVenta):
        if cantVenta <= len(self.stock):
        



"""n=Negocio()
print(n.talle)"""

    

    

#caja = 30000
 #   talle = ["S","M","L","XL"]
  #  precioCompra = [500,600,700,800]
   # precioVenta = [1500,1800,2100,2400]
    #cantidad = [100,200,200,100]
        
    
