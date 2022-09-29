class Utiles():
    def mostrar(msj,lissta):
        print(f"{msj}:")
        for i in lissta:
            print(f" {i}")

class Producto():
    def __init__(self,id,nombre_prod,stock,precio) -> None:
        self.id = id
        self.nombre_prod = nombre_prod
        self.stock = stock
        self.precio = precio
    
    def __repr__(self) -> str:
        return f"{self.id} {self.nombre_prod} {self.stock} {self.precio}"

class Empresa():
    def __init__(self,nombre_emp) -> None:
        self.nombre_emp = nombre_emp
        self.caja = 100000
        self.listaProd = []
        self.listadatos = [(0,"Remera Lisa",10,1000),(1,"Remera Estampada",20,2000),(2,"Jean",30,3000),(3,"Gabardina",40,4000)]
    
    def cargaProducto(self):
        for elemento in self.listadatos:
            p = Producto(*elemento)
            self.listaProd.append(p)

    def ventaProd(self):
        nProd = [elemento.nombre_prod for elemento in self.listaProd]
        nId = [(elemento.nombre_prod,elemento.id) for elemento in self.listaProd]
        x = input("Que producto desea vender: ")
        while x not in nProd:
            print(f"El producto {x} no existe")
            Utiles.mostrar("Prductos disponibles: ",nProd)
            x = input("Que producto desea vender: ")
        pos = 0
        for i in nId:
            if i[0] == x:
                pos = i[1]
        cant = int(input("Que cantidad desea vender?: "))
        if cant > self.listaProd[pos].stock:
            print(f"No hay existencia suficiente. Se anula la operación de venta de {cant} {x}")
        else:
            precio = self.listaProd[pos].precio
            totalVenta = cant * precio
            self.caja = self.caja + totalVenta
            self.listaProd[pos].stock = self.listaProd[pos].stock - cant
            print(f"Venta: {x} / Stock: {self.listaProd[pos].stock} / Caja: {self.caja}")
            print(" ")
  
    def inventario(self):
        print(f"Inventario de {self.nombre_emp}:")
        for producto in self.listaProd:
            print(f"Articulo: {producto.id + 1} - {producto.nombre_prod} - {producto.precio} - Stock:{producto.stock}")

# Prog ppal
c = Empresa("Negocio Triple XXX")
c.cargaProducto()
c.ventaProd() # 15 Jean
c.ventaProd()  # 10 Remera Lisa
c.ventaProd()  # 20 Jean
c.ventaProd()  # 20 Gabardina
c.inventario()
