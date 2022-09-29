from dataclasses import dataclass

@dataclass
class Producto:
    id: int
    stock: int
    precio: int

class Negocio:
    def __init__(self, n, SI):
        self.nombre = n
        self.saldoInicial= SI
        self.listaProductos =[["1.Remera Lisas",10, 1000],["2.REmera Estampadas",20, 2000],["3.Jean",30, 3000],["4.Gabardina",40, 4000]]
        self.productos= []
        for p in self.listaProductos:
            objProducto = Producto(p[0],p[1],p[2])
            self.productos.append(objProducto)
        
    def venta(self,tipo,cant):
        for p in self.productos:
            nombreProducto = p.id[2:]
            if tipo == nombreProducto:
                if p.stock < cant:
                    print(f"No hay existencia suficiente. Se anula la operación de venta de {cant} {nombreProducto}")
                else:
                    p.stock -= cant
                    self.saldoInicial += (cant*p.precio)
                    print(f"Venta: {cant} {nombreProducto}  | Stock actualizado: {p.stock} | Caja: {self.saldoInicial}")
    def __str__(self):
        cadena = ""
        for p in self.productos:
            cadena += f"Articulo #{p.id[:1]} - {p.id[2:]} - Precio: {p.precio}. Stock: {p.stock}\n"
        cadena+= f"Saldo: {self.saldoInicial}"
        return cadena


Empresa = Negocio("Triple XXX", 100000)
Empresa.venta("Jean", 15)
Empresa.venta("Remera Lisas", 10)
Empresa.venta("Jean", 20)
Empresa.venta("Gabardina", 20)
print("Inventario Completo")
print(Empresa)