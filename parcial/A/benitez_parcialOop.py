from dataclasses import dataclass
from random import choice


@dataclass
class Remera:
    precioCompr_S: int = 500
    '''precioCompr_M: int = 600
    precioCompr_L: int = 700
    precioCompr_XL: int = 80
    '''
    color: str = str(choice(["Blanco", "Negro", "Azul"]))


@dataclass
class Negocio:
    caja = float = 30000
    precioVenta_S: int = 1500

    stock = [Remera() for i in range(100)]
    '''stock1 = {"S": [Remera("S") for i in range(100)],
              "M": [Remera("M") for i in range(200)],
              "L": [Remera("L") for i in range(200)],
              "XL": [Remera("XL") for i in range(100)]
              }
'''

    def comprar(self, cantCompra):
        if cantCompra * 500 <= self.caja:
            self.stock += [Remera() for i in range(cantCompra)]
            self.caja -= 500 * cantCompra
            print(
                f"Se compraron {cantCompra} remeras. El nuevo stock es {len(self.stock)}. La caja esta en ${self.caja} -------")
        else:
            print(
                f"El fondo disponible es de ${self.caja}, No es suficiente para comprar {cantCompra} remeras.")

    def vender(self, cantVenta):
        if cantVenta <= len(self.stock):
            del self.stock[:cantVenta]
            self.caja += self.precioVenta_S * cantVenta
            print(
                f"Se vendedieron {cantVenta} remeras. Por un total de ${self.precioVenta_S*cantVenta} y la caja quedó en ${self.caja} ------"
            )
        else:
            print(f"No es posible efectuar la compra\nStock insuficiente")

    def estado(self):
        print(f"Estado Final. Caja: ${self.caja}")
        print(
            f"Remeras (talle = S, Precio de venta = {self.precioVenta_S}, cantidad = {len(self.stock)})")


if __name__ == "__main__":
    negocio = Negocio()
    negocio.vender(100)
    negocio.comprar(21)
    negocio.vender(201)
    negocio.estado()
