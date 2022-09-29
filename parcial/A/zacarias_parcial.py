class Negocio:
    def __init__(self, name):
        self.name = name
        self.caja = 30000        
        self.stock = [
            {"talle": "S", "precioCompra": 500, "precioVenta": 1500, "cantidad": 100},
            {"talle": "M", "precioCompra": 600, "precioVenta": 1800, "cantidad": 200},
            {"talle": "L", "precioCompra": 700, "precioVenta": 2100, "cantidad": 200},
            {"talle": "XL", "precioCompra": 800, "precioVenta": 2400, "cantidad": 100},
        ]
        self.talles = ['S', 'M', 'L', 'XL']

    def compra(self, cant, talle):
        stack = self.stock[self.talles.index(talle)]
        monto = stack['precioCompra'] * cant
        if self.caja >= monto:
            self.caja -= monto
            stack['cantidad'] += cant 
            return f'Venta: {cant} remeras de talle {talle} | Stock actualizado: {stack["cantidad"]} | Caja: {self.caja}'
        else: return f'No hay dinero suficiente.\nSe anula la operación de compra de {cant} remeras de talle {talle}.'


    def venta(self, cant, talle):
        stack = self.stock[self.talles.index(talle)]
        if cant <= stack['cantidad']:
            stack['cantidad'] -= cant
            self.caja += stack['precioVenta'] * cant
            return f'Venta: {cant} remeras de talle {talle} | Stock actualizado: {stack["cantidad"]} | Caja: {self.caja}'
        else: 
            return f'No hay existencia suficiente.\nSe anula la operación de venta de {cant} remeras de talle {talle}.'

    def __str__(self):
        out = f'\nEstado del {self.name}. Caja: {self.caja}'
        for stack in self.stock:
            out += f'\n{stack}'
        return out + '\n'

negocio = Negocio('Negocio')
print(negocio)
print(negocio.venta(100, 'L'))
print(negocio.compra(100, 'S'))
print(negocio.venta(50, 'M'))
print(negocio.compra(100, 'XL'))
print(negocio.venta(200, 'M'))
print(negocio.compra(50, 'L'))
print(negocio)