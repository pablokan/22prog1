from dataclasses import dataclass

@dataclass
class Productos:
    id:int
    nombre:str
    stock:int
    precio:int

@dataclass
class Negocio:
    def __init__(self, n ,c):
        self.Nombre=n
        self.Caja=c
        self.listaProductos=[1,"Remera Lisa",10,1000],[2,"Remera estampadas",20,2000],[3,"Jean",30,3000],[4,"Gabardinas",40,4000]
        self.productos=[]
        for prod in self.listaProductos:
            ObjetoProducto=Productos(prod[0],prod[1],prod[2],prod[3])
            self.productos.append(ObjetoProducto)
        

    def ventas(self,tipo,cantidad):
        for p in self.productos:
            if tipo == p.nombre:
                if p.stock < cantidad:
                    print(f"No hay existencia suficiente. Se anula la operación de venta de {cantidad} {p.nombre}")
                else:
                    p.stock -= cantidad
                    self.Caja+=(cantidad*p.precio)
                    print(f"Venta: {cantidad} {p.nombre} | Stock actualizado: {p.stock}| Caja: {self.Caja}")
    def __str__(self):
        Texto=""
        for p in self.productos:
            Texto += f"articulo #{p.id} - {p.nombre} - Precio: {p.precio} Stock {p.stock}\n"
        return Texto

Triple=Negocio("Triple XXX", 100000)
Triple.ventas("Jean", 15)
Triple.ventas("Remera Lisa",10)
Triple.ventas("Jean",20)
Triple.ventas("Gabardinas",20)
print()
print("Inventario Completo")
print(Triple)