from dataclasses import dataclass

@dataclass
class Remera:
    talle: str
    precioCompra: int = None
    precioVenta: int = None
    cantidad: int = None

@dataclass
class Remeralandia:
    cajaActual: int = 30000
    #stock = [Remera("s") for i in range(100)], [Remera("m") for e in range(200)], [Remera("l") for x in range(200)], [Remera("xl") for x in range(100)]
    """stock = [["S",500,1500,100]
        ["M",600,1800,200]
        ["L",700,2100,200]
        ["XL",800,2400,100]] """

    def __post_init__(self):
        datosS = ["S",500,1500,100]
        remerasS = []
        datosM = ["M",600,1800,200]
        remerasM = []
        for i in range(100):
            self.talle = datosS[i][0]
            self.precioCompra = datosS[i][1]
            self.precioVenta = datosS[i][2]
            self.cantidad = datosS[i][3]
            remS = Remera(self.talle,self.precioCompra,self.precioVenta,self.cantidad)
            remerasS.append(remS)
        for e in range(200):
            self.talle = datosM[e][0]
            self.precioCompra = datosM[e][1]
            self.precioVenta = datosM[e][2]
            self.cantidad = datosM[e][3]
            remM = Remera(self.talle,self.precioCompra,self.precioVenta,self.cantidad)
            remerasM.append(remM)

    def comprar(self, cantidadCompra, talle):
        costo = self.stock[talle][0].precio
        if cantidadCompra * costo <= self.cajaActual:
            self.stock[talle] += [Remera(talle) for i in range(cantidadCompra)]
            self.cajaActual -= costo * cantidadCompra
            print(f"Compra: {cantidadCompra} remeras de talle {talle} | Stock actualizado: {len(self.stock[talle])} talle {talle} | Caja: {self.cajaActual}\n")
        else:
            print(f"El fondo disponible es de ${self.cajaActual}, no es suficiente para comprar {cantidadCompra} remeras talle de {talle}.\n")
        
emp1 = Remeralandia()
emp1.comprar(100,"s")
    