class Ropa:
    def __init__(self, id, nombre, precio, stock) -> None:
        self.id= id
        self.nombre = nombre
        self.precio = precio    
        self.stock = stock
        

class Remera(Ropa):
    def __init__(self, id, nombre, precio, stock) -> None:
        super().__init__(id, nombre, precio, stock)
    
class Pantalon(Ropa):
    def __init__(self, id, nombre, precio, stock) -> None:
        super().__init__(id, nombre, precio, stock)

class Tienda():
    def __init__(self) -> None:
        self.saldo = 100000
        existencias = []
        self.existencias = existencias
        self.stock = [ ['remera lisa', 10, 1000],
                ['remera estampada', 20, 2000],
                ['jean', 30, 3000],
                ['gabardina', 40, 4000]
                ]

    
    def cargaStock (self):
        for x in range(len(self.stock)):
            a = Ropa(x+1, self.stock[x][0],self.stock[x][2],self.stock[x][1])
            self.existencias.append(a)
    
    def mostrarProductos(self):
        print('Productos:')
        for x in range(len(self.stock)):
            print(f'#{x+1} -{self.stock[x][0]}')


    def venta(self, prod, cant):
        for x in range(len(self.existencias)):
            if prod == self.existencias[x].id:
                if self.existencias[x].stock >= cant:
                    self.existencias[x].stock = self.existencias[x].stock - cant
                    self.saldo = self.saldo + (self.existencias[x].precio*cant)
                    print(f'Venta: {cant} {self.existencias[x].nombre}  | Stock actualizado: {self.existencias[x].stock} | Caja: ${self.saldo}')
                else:
                    print(f'No hay existencia suficiente. Se anula la operación de venta de {cant} {self.existencias[x].nombre}')
    
    def mostrarStock(self):
        print('Inventario Completo: ')
        for ropita in self.existencias:
            print(f'Articulo #{ropita.id} - {ropita.nombre} - Precio: {ropita.precio}. Stock: {ropita.stock}')

tienda1 = Tienda()

tienda1.cargaStock()
tienda1.mostrarProductos()
tienda1.venta(3,15)
tienda1.venta(1,10)
tienda1.venta(3,20)
tienda1.venta(4,20)
tienda1.mostrarStock()
