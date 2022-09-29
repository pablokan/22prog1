
class Remera:
    def __init__(self,precioL,stockL,precioE, stockE) -> None:
        self.precioLisa = precioL
        self.stockLisa = stockL
        self.precioEstamp = precioE
        self.stockEstamp = stockE

class Pantalon:
    def __init__(self, precioJ,stockJ, precioG, stockG) -> None:
        self.precioJean = precioJ
        self.stockJean = stockJ
        self.precioGabar = precioG
        self.stockG = stockG
        
class Tienda:
    def __init__(self) -> None:
        self.caja = 100000
        self.precioJeans = 3000
        self.stockJeans = 30
        self.precioGabardina = 4000
        self.stockGabardina = 40
        self.precioLisa = 1000
        self.stockLisa = 10
        self.precioEstampada = 2000
        self.stockEstampada = 20
        self.j = Pantalon(self.precioJeans,30, self.precioGabardina, 40)
        self.r = Remera(self.precioLisa,10,self.precioEstampada,20)
        self.listaJeans = []
        self.listaGabardinas = []
        self.listaLisas = []
        self.listaEstampadas = []
    def ventaJean(self, cantidad):
        if self.j.stockJean > cantidad:
            venta = cantidad
            stockNuevo = int(self.j.stockJean - cantidad)
            ingreso = int(self.j.precioJean * cantidad)
            cajaNueva = int(self.caja + ingreso)
            print(f"Venta de jean: {venta}, Stock Actualizado: {stockNuevo}, Caja: {cajaNueva}")
        else:
            print("Stock no disponible")
    def ventaJean2(self, cantidad):
        if self.j.stockJean > cantidad:
            venta = cantidad
            stockNuevo = int(self.j.stockJean - cantidad)
            ingreso = int(self.j.precioJean * cantidad)
            cajaNueva = int(self.caja + ingreso)
            print(f"Venta de jean: {venta}, Stock Actualizado: {stockNuevo}, Caja: {cajaNueva}")
        else:
            print("Stock no disponible")
    def ventaGabar(self, cantidad):
        if self.j.stockG > cantidad:
            venta = cantidad
            stockNuevo = int(self.j.stockG - cantidad)
            ingreso = int(self.j.precioGabar * cantidad)
            cajaNueva = int(self.caja + ingreso)
            print(f"Venta de Gabardina: {venta}, Stock Actualizado: {stockNuevo}, Caja: {cajaNueva}")
        else:
            print("Stock no disponible")

    def ventaLisas(self, cantidad):
        if self.r.stockLisa >= cantidad:
            venta = cantidad
            stockNuevo = int(self.r.stockLisa - cantidad)
            ingreso = int(self.r.precioLisa * cantidad)
            cajaNueva = int(self.caja + ingreso)
            print(f"Venta de Remeras Lisas: {venta}, Stock Actualizado: {stockNuevo}, Caja: {cajaNueva}")
        else:
            print("Stock no disponible")
    def ventaEstampadas(self, cantidad):
            if self.r.stockEstamp >= cantidad:
                venta = cantidad
                stockNuevo = int(self.r.stockEstamp - cantidad)
                ingreso = int(self.r.precioEstamp * cantidad)
                cajaNueva = int(self.caja + ingreso)
                print(f"Venta de Remeras Estampadas: {venta}, Stock Actualizado: {stockNuevo}, Caja: {cajaNueva}")
            else:
                print("Stock no disponible")                

jean1 = Tienda()
jean1.ventaJean(15)
jean2 = Tienda()
jean2.ventaJean2(20)
gabardina = Tienda()
gabardina.ventaGabar(20)
lisas = Tienda()
lisas.ventaLisas(10)
estampadas = Tienda()
estampadas.ventaEstampadas(0)