class Empleado:
    def __init__(self, n) -> None:
        self.nombre = n

class Empresa:
    def __init__(self) -> None:
        self.empleado = Empleado("José")
        #self.empleado = "José"

empresa = Empresa()
print(empresa.empleado.nombre)
#print(empresa.empleado)