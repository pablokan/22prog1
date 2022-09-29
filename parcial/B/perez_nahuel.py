from dataclasses import dataclass


@dataclass
class RemeraLisa:
    stock= 10
    precio=1000

@dataclass
class RemeraEstampada:
    stock = 20
    precio = 2000
@dataclass
class Jeans:
    stock = 30
    precio = 3000
@dataclass
class Garibaldina:
    stock = 40
    precio = 4000        

class Tienda:
    caja = 100000
    def Vender(self,cant,prenda):
        prenda=prenda
        
        if cant>prenda.stock:
            print("No hay stock suficiente, se anula la operacion de venta de",cant,prenda())
        else:
            prenda.stock-=cant
            self.caja+=prenda.precio*cant
            print("Venta de: ",prenda(),"/ Stock actualizado: ", prenda.stock,"/Caja:",self.caja )
            
    def GetName(self):
        print("Inventario Completo")
        print("Articulo 1- remera lisa- precio:",RemeraLisa.precio,"Stock:",RemeraLisa.stock)
        print("Articulo 2- remera estampada- precio:",RemeraEstampada.precio,"Stock:",RemeraEstampada.stock)
        print("Articulo 3- jeans- precio:",Jeans.precio,"Stock:",Jeans.stock)
        print("Articulo 4- garibaldina- precio:",Garibaldina.precio,"Stock:",Garibaldina.stock)


tiendita=Tienda()
tiendita.Vender(15,Jeans)
tiendita.Vender(10,RemeraLisa)
tiendita.Vender(20,Jeans)
tiendita.Vender(20,Garibaldina)
tiendita.GetName()
 
