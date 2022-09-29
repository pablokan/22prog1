from dataclasses import dataclass

@dataclass
class Articulo:
    id: int
    tipoPrenda: str
    stock: int
    precio: int

class Negocio:
    def __init__(self, listaArticulos):
        self.saldoCaja = 100_000
        self.listaArticulos = listaArticulos
        self.articulos = [Articulo(*articulo) for articulo in self.listaArticulos]

    def vender(self, prendaAComprar, cantidad):
        tiposDePrendas = [articulo.tipoPrenda for articulo in self.articulos]
        
        while prendaAComprar not in tiposDePrendas:
            prendaAComprar = input(f"{prendaAComprar} no se encuentra en el inventario. Las opciones son: {tiposDePrendas}. Intentelo nuevamente: ")
        
        for articulo in self.articulos:
            if articulo.tipoPrenda == prendaAComprar and cantidad <= articulo.stock:
                articulo.stock -= cantidad
                self.saldoCaja += cantidad * articulo.precio
                return f"Venta: {cantidad} {articulo.tipoPrenda} | Stock actualizado: {articulo.stock} | Caja: {self.saldoCaja}"
            elif articulo.tipoPrenda == prendaAComprar and cantidad > articulo.stock:
                return f"No hay existencia suficiente. Se anula la operación de venta de {cantidad} {articulo.tipoPrenda}"

    def mostrarInventario(self):
        print("----------INVENTARIO DEL NEGOCIO----------")
        for a in self.articulos:
            print(f"Artículo #{a.id} - {a.tipoPrenda} - Precio: {a.precio} - Stock: {a.stock}.")

listaDeArticulos = [[1, "remera lisa", 10, 1000], [2, "remera estampada", 20, 2000], [3, "jean", 30, 3000], [4, "gabardina", 40, 4000]]

negocio1 = Negocio(listaDeArticulos)
print(negocio1.vender("jean", 15))
print(negocio1.vender("remera lisa", 10))
print(negocio1.vender("jean", 20))
print(negocio1.vender("gabardina", 20))

negocio1.mostrarInventario()