from dataclasses import dataclass



@dataclass

class Negocio:
    CantRemeras:int
    DineroCaja: int


    def Compra(self):
        compraRemeras=input(int("ingrese la cantidad de remeras que desa comprar:"))
        caja=Negocio.DineroCaja-(compraRemeras*500)
        stock=Negocio.CantRemeras+compraRemeras
        print("Cantidad de dinero en la caja: ",caja)
        print("Cantidad de remeras en Stock: ",stock)


    def Venta(self):
        ventaRemera=input(int("ingrese la cantidad de remeras que vendio:"))
        if ventaRemera > Negocio.CantRemeras:
            print("no hay suficientes remeras en stock, se le aplicara un descuento del 10%")
            Ingreso=Negocio.CantRemeras*0.9
            caja=Negocio.DineroCaja+Ingreso
            Negocio.CantRemeras=0
            print("Cantidad de remeras en stock: ",Negocio.CantRemeras)
            print("Cantidad de dinero en la caja:",caja)
        else:
            IngresoS=(ventaRemera*1500)
            caja=Negocio.DineroCaja+IngresoS
            stock=Negocio.CantRemeras-ventaRemera
            print("Cantidad de dinero en la caja: ",caja)
            print("Cantidad de remeras en stock: ", stock)




unNegocio=Negocio(100,30000)

