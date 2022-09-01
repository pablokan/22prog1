class Empleado:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Empresa:
    def __init__(self) -> None:
        self.empleado = Empleado("José") # composición
        #self.empleado = "José" SIN compo

empresa = Empresa()
print(empresa.empleado.nombre)
#print(empresa.empleado)