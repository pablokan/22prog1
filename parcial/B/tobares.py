from dataclasses import dataclass

@dataclass
class Pantalon:
    prenda: str
    precioVenta: int
    cantidad: int

@dataclass
class Remera:
    tipoPrenda: str
    pVenta: int
    cantidad: int

@dataclass
class Empresa:
    caja: int = 30000
    stock = []
    entrada = [["Remera Lisa", 10, 1000], ["Remera Estampada", 20, 2000],["Pantalon Jean", 30, 300], ["Pantalon Gabardina", 40, 4000]]
    for x in range(len(entrada)):
        prenda = entrada[x][0]
        disponibilidad = entrada[x][1]
        pVenta = entrada[x][2]
        remera = Remera(prenda, pVenta, disponibilidad)
        pantalon = Pantalon(prenda, pVenta, disponibilidad)
        stock.append(remera)

    def estadoEmp(self):
        print(f"Estado Empresa. Caja: {self.caja}")
        for x in self.stock:
            print(x)
        print()

    def venta(self, cantidad, tipoPrenda):
        self.cantidad = cantidad
        self.tipoPrenda = tipoPrenda
        for remera in self.stock:
            if self.tipoPrenda == remera.tipoPrenda:
                if self.cantidad < remera.cantidad:
                    total = remera.pVenta * self.cantidad
                    self.caja += total
                    remera.cantidad -= self.cantidad
                    print(f"Venta: {self.cantidad} remeras talle {self.tipoP}| Stock Actualizado: {remera.cantidad} | Caja: {self.caja}\n")
                else:
                    print(f"No hay existencia suficiente.\nSe anula la operación de venta de {self.cantidad} remeras de talle {self.tipoPrenda}\n")

