from dataclasses import dataclass

@dataclass
class Articulo:
    id: int
    nombre: str
    precio: float
    cantidad: int

    def __str__(self) -> str:
        return f"Artículo #{self.id} - {self.nombre} - Precio: {self.precio}. Stock: {self.cantidad}"

@dataclass
class Negocio:
    stock: list[dict]
    caja: int = 100_000

    def __post_init__(self):
        self.articulos = [Articulo(**articulo) for articulo in self.stock]

    def venta(self, c, a):
        for articulo in self.articulos:
            if articulo.nombre == a:
                if articulo.cantidad >= c:
                    print(f"\nVenta: {c} {a} ", end=" | ")
                    articulo.cantidad -= c
                    print(f"Stock actualizado: {articulo.cantidad}", end=" | ")
                    self.caja += articulo.precio * c
                    print(f"Caja: {self.caja}")
                else:
                    print(f"\nNo hay existencia suficiente. Se anula la operación de venta de {c} {a}")
        
    def getAll(self):
        print("\n\nInventario Completo")
        for articulo in self.articulos:
            print(articulo)

    
stock = [
    {"id": 1, "nombre": "remera lisa", "precio": 1000, "cantidad": 10},
    {"id": 2, "nombre": "remera estampada", "precio": 2000, "cantidad": 20},
    {"id": 3, "nombre": "jean", "precio": 3000, "cantidad": 30},
    {"id": 4, "nombre": "gabardina", "precio": 4000, "cantidad": 40},
]
negocio = Negocio(stock)
negocio.venta(15, "jean")
negocio.venta(10, "remera lisa")
negocio.venta(20, "jean")
negocio.venta(20, "gabardina")
negocio.getAll()