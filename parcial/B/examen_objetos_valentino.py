from dataclasses import dataclass

@dataclass
class Articulo:
    pass
     

@dataclass
class Negocio():
    saldo = 100_000

    stockRemeras = {
    "lisas": [10, 1000],
    "estampadas": [20, 2000],
    }

    stockPantalones = {
    "jean": [30, 3000],
    "gabardina":[40, 4000],
    }                      



    def ventas(self, cantidad, articulo, tipo):
        if articulo == 'pantalones':
            self.stock = self.stockPantalones[tipo][0]
            self.precio = self.stockPantalones[tipo][1]
        elif articulo == 'remeras':
            self.stock = self.stockRemeras[tipo][0]
            self.precio = self.stockRemeras[tipo][1]

        if cantidad > self.stock:
            print(f'No hay existencia suficiente. Se anula la operación de venta de {cantidad} {tipo}')
        
        else:
            costeDeTransaccion = cantidad * self.precio
            self.saldo += costeDeTransaccion
            self.stock -= cantidad

            if articulo == 'pantalones':
                self.stockPantalones[tipo][0] = self.stock
            elif articulo == 'remeras':
                self.stockRemeras[tipo][0] = self.stock
            
            print(f'Venta: {cantidad} {articulo} {tipo}  | Stock actualizado: {self.stock} | Caja: {self.saldo}')


    # def inventatioCompleto(self):
    #     print('inventario completo: ')
    #     for articulo in self.stockRemeras.items:
    #         print(f'Artículo - {} - Precio: {}. Stock: {}')
        
        # for keys in self.stockPantalones:
        #     print(f'Artículo - {} - Precio: {}. Stock: {}')


tate = Negocio()

tate.ventas(15, 'pantalones', 'jean')
tate.ventas(10, 'remeras', 'lisas')
tate.ventas(20, 'pantalones', 'jean')
tate.ventas(20, 'pantalones', 'gabardina')

# tate.inventatioCompleto()

