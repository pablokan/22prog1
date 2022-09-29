# PARCIAL OOB LUCA PETROCCHI COMISIÓN B

diccionario_de_ids = {1: "Lisas", 2: "Estampadas", 3: "Jeans", 4: "Gabardinas"}

class Ropa:
    def __init__(self, sto, pre, id):
        self.stock = sto
        self.precio = pre
        self.idNum = id
        self.caja = 100000

class Lisas(Ropa):
    def __init__(self, sto, pre):
        super().__init__(sto, pre, 1)

class Estampadas(Ropa):
    def __init__(self, sto, pre):
        super().__init__(sto, pre, 2)

class Jeans(Ropa):
    def __init__(self, sto, pre):
        super().__init__(sto, pre, 3)

class Gabardinas(Ropa):
    def __init__(self, sto, pre):
        super().__init__(sto, pre, 4)

class General: 
    def __init__(self):
        L = Lisas(10, 1000)
        E = Estampadas(20, 2000)
        J = Jeans(30, 3000)
        G = Gabardinas(40, 4000)
        self.todosLosProductos = [L, E, J, G]

    def estado(self):
        print("Inventario Completo")
        for x in range(len(diccionario_de_ids)):
            producto = self.todosLosProductos[x]
            print(f"Artículo {x+1} - {diccionario_de_ids[x+1]} - Precio: ${producto.precio}. Stock: {producto.stock}")

    def venta(self, cantidad, id):
        producto = self.todosLosProductos[id]
        if producto.stock < cantidad:
            print(f"Venta de {cantidad} {diccionario_de_ids[producto.idNum]} cancelada. No hay existencias suficientes.")
        else:
            ganancia = cantidad * producto.precio
            producto.stock -= cantidad
            producto.caja += ganancia
            print(f"Venta: {cantidad} {diccionario_de_ids[producto.idNum]} | Stock actualizado: {producto.stock} | Caja: ${producto.caja}")


tienda = General()
tienda.venta(15, 2)
tienda.venta(10, 0)
tienda.venta(20, 2)
tienda.venta(20, 3)
print("---------------------------------------")
tienda.estado()

