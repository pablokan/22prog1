from dataclasses import dataclass
from random import choice

@dataclass
class Remeras:
    talle: str 
    color: str = str(choice(["Verde", "Azul", "Rojo", "Blanco"]))
    precio: int = None
    def _post_init_(self):
        if self.talle == "s":
            self.precio = 500
        if self.talle == "m":
            self.precio = 600
        if self.talle == "l":
            self.precio = 700
        if self.talle == "xl":
            self.precio = 800
    
@dataclass
class Remeralandia:
    cajaIn: int = 30000
    precio_Venta = {'s':1500,'m':1800,'l':2100,'xl':2400}
    stockRem = {'s':[Remeras('s') for s in range(100)],'m':[Remeras('m') for m in range(200)],'l':[Remeras('l') for j in range(200)],'xl':[Remeras('xl') for l in range(100)]}

  
    
    def compra(self, cantCom, talle):
        costo=self.stockRem[talle][0].precio
        if cantCom * costo <= self.cajaIn:
            self.stockRem[talle]+= [Remeras(talle) for i in range(cantCom)]
            self.cajaIn -= costo*cantCom
            print(f'Compra: {cantCom} remeras de talle: {talle}  Stock actualizado: {len(self.stockRem[talle])} la caja es de:  {self.cajaIn}\n')
        else:
            print(f"El fondo disponible ${self.cajaIn}, no es suficiente para comprar {cantCom} remeras.\n")
            
    def venta(self, cntVenta,talles):
        if cntVenta <= len(self.stockRem[talles]):
            del self.stockRem[talles][:cntVenta]
            self.cajaIn += self.precio_Venta[talles]*cntVenta
            print(f'Venta: {cntVenta}, remeras de talle {talles}, Stock actualizado: {len(self.stockRem[talles])}, Caja: {self.cajaIn}')
        else:
            print(f"La cantidad requerida de {cntVenta} remeras es superior al stock. OPERACION ANULADA")
    def estadoFinal(self): 
        print(f"estado final{self.cajaIn}")
        for i in self.precio_Venta:
            for x in self.stockRem:
                print(f'Talle: {i} - Precio de Compra: {self.stockRem[x][0].precio} - Precio de Venta: {self.precio_Venta[i]} - Stock: {len(self.stockRem[i])}')
                break
negocio = Remeralandia()           
negocio.venta(100, "l")
negocio.compra(100, "s")
negocio.venta(50, "m")
negocio.compra(100, "xl")
negocio.venta(200, "m")
negocio.compra(50, "l")