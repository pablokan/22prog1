from dataclasses import dataclass

@dataclass
class Ropa:
    id : int
    articulos: str
    stock: int
    precioVenta: int

@dataclass
class Remera(Ropa):
    def __str__(self):
        return f"Articulo #{self.id}: {self.articulos} - Precio: {self.precioVenta} - {self.stock}"

@dataclass
class Pantalon(Ropa):
    def __str__(self):
        return f"Articulo #{self.id}: {self.articulos} - Precio: {self.precioVenta} - {self.stock}"

class Negocio:
    def __init__(self):
        self.cajaInicial = 100_000
        self.listaRemeras = []
        self.listaPantalones = []
        remeras = [[1,"Remera lisa", 10, 1000],
                [2,"Remera estampada", 20, 2000]]
        pantalones = [[3,"Pantalon jean", 30, 3000],
                    [4,"Pantalon gabardina", 40, 4000]]

        for ropaRemera in remeras:
            r = Remera(*ropaRemera)
            self.listaRemeras.append(r)
        for ropaPantalon in pantalones:
            p = Pantalon(*ropaPantalon)
            self.listaPantalones.append(p)
        
    def ventas(self,cantidad,tipo):
        todos = self.listaRemeras + self.listaPantalones
        for prenda in todos:
            if prenda.articulos == tipo and cantidad <= prenda.stock:
                venta = cantidad * prenda.precioVenta
                self.cajaInicial += venta
                prenda.stock-= cantidad
                print(f"Venta: {prenda.articulos}| Stock Actualizado: {prenda.stock}| Caja: {self.cajaInicial}")
            elif cantidad > prenda.stock and prenda.articulos == tipo:
                print("No hay existencia suficiente. Se anula la operación de venta de 20 jean")
                
    def mostrarInventario(self):
        print("Inventario Completo")
        todosx2 = self.listaRemeras + self.listaPantalones
        for prenda in todosx2:
            print(prenda)

rockaBruja = Negocio()
rockaBruja.ventas(15,"Pantalon jean")
rockaBruja.ventas(10,"Remera lisa")
rockaBruja.ventas(20,"Pantalon jean")
rockaBruja.ventas(20,"Pantalon gabardina")
rockaBruja.mostrarInventario()

