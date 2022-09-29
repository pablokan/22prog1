from dataclasses import dataclass
 
@dataclass
class Remera:
   precioLisa = 1000
   stockLisa = 10
   precioEstampada = 2000
   stockEstampada = 20
   stockRemeras = 30
 
@dataclass
class Pantalon:
   precioJean = 3000
   stockJean = 30
   precioGabardina = 4000
   stockGabardina = 40
   stockPantalones = 70
 
@dataclass
class Tienda(Remera, Pantalon):
   cajaInicial = 100000
   remera = Remera()
   pantalones = Pantalon()
 
 
 
   def venderRemeraLisa(self, cantidad):
       precioTotalLisa = int(self.remera.precioLisa * cantidad)
       nuevaCantidadLisas = (self.stockLisa - cantidad)
       self.cajaInicial += precioTotalLisa
       print(f"Se vendieron {cantidad} de remeras Lisas | Stock actualizado: {nuevaCantidadLisas} | Caja: {self.cajaInicial}")
 
   def venderRemeraEstampada(self, cantidad):
       precioTotalEstampada = int(self.remera.precioEstampada * cantidad)
       nuevaCantidadEstampadas = (self.stockEstampada - cantidad)
       self.cajaInicial += precioTotalEstampada
       print(f"Se vendieron {cantidad} de remeras Estampadas | Stock actualizado: {nuevaCantidadEstampadas} | Caja: {self.cajaInicial}")
 
   def venderJean(self, cantidad):
       precioTotalJeans = int(self.pantalones.precioJean * cantidad)
       nuevaCantidadJeans = (self.stockJean - cantidad)
       if cantidad > nuevaCantidadJeans:
           print(f"No hay existencia suficiente. Se anula la operación de venta de 20 jean")
       else:
            self.cajaInicial += precioTotalJeans
            print(f"Se vendieron {cantidad} de Jeans | Stock actualizado: {nuevaCantidadJeans} | Caja: {self.cajaInicial}")
 
 
   def venderGabardina(self, cantidad):
       precioTotalGabardina = int(self.pantalones.precioGabardina * cantidad)
       nuevaCantidadGabardina = (self.stockGabardina - cantidad)
       self.cajaInicial += precioTotalGabardina
       print(f"Se vendieron {cantidad} de Gabardinas | Stock actualizado: {nuevaCantidadGabardina} | Caja: {self.cajaInicial}")
 
   def mostrarInventarioCompleto(self):
       print("Inventario completo")
       print(f"Articulo #1 - remera lisa - Precio: {self.precioLisa} - Stock: {self.nuevaCantidadLisas}")
       print(f"Articulo #2 - remera estampada - Precio: {self.precioEstampada} - Stock: {self.nuevaCantidadEstampadas}")
       print(f"Articulo #3 - Jeans - Precio: {self.precioJean} - Stock: {self.nuevaCantidadJeans}")
       print(f"Articulo #4 - Gabardina - Precio: {self.precioGabardina} - Stock: {self.nuevaCantidadGabardinas}")
 
tienda1 = Tienda()
 
tienda1.venderJean(15)
tienda1.venderRemeraLisa(10)
tienda1.venderGabardina(20)
tienda1.mostrarInventarioCompleto()
