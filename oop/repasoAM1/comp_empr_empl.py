class Empleado:
    def __init__(self, n, s) -> None:
        self.nombre = n
        self.sueldo = s

class Empresa:
    def __init__(self) -> None:
        self.empleado = Empleado("Juan", 120_000) # composición

    def getSalary(self):
        return self.empleado.sueldo


empresa = Empresa()
print(empresa.empleado.sueldo)
print(empresa.getSalary())
