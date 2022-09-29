# Héctor González

from dataclasses import dataclass
from random import choice

@dataclass
class Remera:
    talle: str
    color = str(choice(('Azul','Rojo','Verde','Negro')))
    precio: int = None

    def __post_init__(self):
        match self.talle.upper():
            case 'S':
                self.precio=500
            case 'M':
                self.precio=600
            case 'L':
                self.precio=700
            case 'XL':
                self.precio=800

@dataclass
class Remeralandia:
    precioVenta = {'s':1500,'m':1800,'l':2100,'xl':2400}
    cajaActual: int = 30000
    stock = {'s':[Remera('s') for i in range(100)],'m':[Remera('m') for j in range(200)],'l':[Remera('l') for j in range(200)],'xl':[Remera('xl') for l in range(100)]}


    def comprar(self,cantCompra,talle): # metodo para comprar y actualizar el stock
        valor=self.stock[talle.lower()][0].precio
        if cantCompra*valor<=self.cajaActual:
            self.stock[talle]+=[Remera(talle) for i in range(cantCompra)]
            self.cajaActual-=valor*cantCompra
            print(f'Compra: {cantCompra} remeras de talle {talle.upper()} | Stock actualizado: {len(self.stock[talle])} talle {talle.upper()} | Caja: {self.cajaActual}\n')
        else:
            print(f'El fondo disponible es ${self.cajaActual}, no es insuficiente para comprar {cantCompra} remeras talle {talle.upper()}.\n')
        
    def vendeer(self,cantVenta,size):
            if cantVenta<=len(self.stock[size]):
                del self.stock[size][:cantVenta]
                self.cajaActual+=self.precioVenta[size]*cantVenta
                print(f'Venta: {cantVenta} remeras de talle {size.upper()} | Stock actualizado: {len(self.stock[size])} | Caja: {self.cajaActual}\n')
            else:
                print('No hay existencia suficiente.')
                print(f'Se anula la operación de venta de {cantVenta} remeras de talle {size.upper()}\n')

    def estado(self):
        print(f'Estado Final. Caja: {self.cajaActual}')
        for j,k in zip(self.stock,self.precioVenta):
            print(f'Talle: {k.upper()} - Precio de Compra: {self.stock[j][0].precio} - Precio de Venta: {self.precioVenta[k]} - Stock: {len(self.stock[k])}')


if __name__=='__main__':
    emp=Remeralandia()
    emp.vendeer(100,'l')
    emp.comprar(100,'s')
    emp.vendeer(50,'m')
    emp.comprar(100,'xl')
    emp.vendeer(200,'m')
    emp.comprar(50,'l')
    emp.estado()
