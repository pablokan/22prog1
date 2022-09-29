# El stock inicial con sus precios es el siguiente:
# Remeras: 1. Lisas  stock = 10 , precio = 1000

# 2. Estampadas stock = 20 , precio = 2000

# Pantalones: 3. jean  stock = 30 , precio = 3000
# 4. Gabardina  stock = 40 , precio = 40000

#Y el saldo inicial de la Caja es de $100.000.

# Crear los objetos correspondientes para cada artículo.

# Hacer métodos para las operaciones que siguen:

# Realizar las siguientes operaciones:

# Venta de 15 jeans
# Venta de 10 remeras lisas
# Venta de 20 jeans
# Venta de 20 gabardinas
# Mostrar estado general



from dataclasses import dataclass

@dataclass
class stock:
    Pantalones: str
    remeras: str

@dataclass
class ValorCaja:
    caja: int = 100_000

@dataclass
class venta_y_stock_prendas(stock):
    stock_lisas: int = 10
    stock_estampadas: int = 20
    precio_lisas: int = 1000
    precio_estampadas: int = 2000
    stock_jean: int = 30
    precio_jean: int = 3000
    stock_gabardina: int = 40
    precio_gabardina: int = 4000
#Salida Esperada:
# Venta: 15 jean  | Stock actualizado: 15 | Caja: 145000
# Venta: 10 remera lisa  | Stock actualizado: 0 | Caja: 155000
# No hay existencia suficiente. Se anula la operación de venta de 20 jean
# Venta: 20 gabardina  | Stock actualizado: 20 | Caja: 235000

@dataclass 
class ventas (venta_y_stock_prendas):
    def venta(self, ordenDeVenta_Jeans):
        ValorCaja = ordenDeVenta_Jeans * self.precio_jean            
        return ValorCaja
    def venta(self, ordenDeVenta_Jeans):
        StockActualizado_jean = self.stock_jean - ordenDeVenta_Jeans
        return StockActualizado_jean
        if StockActualizado_jean > ordenDeVenta_Jeans:
            

    def venta(self, ordenDeVenta_Remera_lisa):
        ValorCaja = ordenDeVenta_Remera_lisa * self.precio_estampadas
        return ValorCaja
    


        







