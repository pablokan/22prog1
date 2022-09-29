from dataclasses import dataclass

@dataclass
class Remera:
    talle: str
    pCompra: int
    pVenta: int
    cantidad: int

@dataclass
class Empresa:
    caja: int = 30000
    stock = []
    entrada = [["S", 500, 1500, 100], ["M", 600, 1800, 200],["L", 700, 2100, 200], ["XL", 800, 2400, 100]]
    for x in range(len(entrada)):
        talle = entrada[x][0]
        pCompra = entrada[x][1]
        pVenta = entrada[x][2]
        cantidad = entrada[x][3]
        remera = Remera(talle, pCompra, pVenta, cantidad)
        stock.append(remera)

    def estadoEmp(self):
        print(f"Estado Empresa. Caja: {self.caja}")
        for x in self.stock:
            print(x)
        print()

    def compra(self, cantidad, talle):
        self.cantidad = cantidad
        self.talle = talle
        for remera in self.stock:
            if self.talle == remera.talle:
                total = remera.pCompra * self.cantidad
                self.caja -= total
                remera.cantidad += self.cantidad
                print(f"Compra: {self.cantidad} remeras talle {self.talle}| Stock Actualizado: {remera.cantidad} | Caja: {self.caja}\n")


    def venta(self, cantidad, talle):
        self.cantidad = cantidad
        self.talle = talle
        for remera in self.stock:
            if self.talle == remera.talle:
                if self.cantidad < remera.cantidad:
                    total = remera.pVenta * self.cantidad
                    self.caja += total
                    remera.cantidad -= self.cantidad
                    print(f"Venta: {self.cantidad} remeras talle {self.talle}| Stock Actualizado: {remera.cantidad} | Caja: {self.caja}\n")
                else:
                    print(f"No hay existencia suficiente.\nSe anula la operación de venta de {self.cantidad} remeras de talle {self.talle}\n")

remeralandia = Empresa()
remeralandia.estadoEmp()
remeralandia.venta(100, "L")
remeralandia.compra(100, "S")
remeralandia.venta(50, "M")
remeralandia.compra(100, "XL")
remeralandia.venta(200, "M")
remeralandia.compra(50, "L")
remeralandia.estadoEmp()