class Empleado:
    def __init__(self, n, s) -> None:
        self.nombre = n
        self.sueldo = s

    def premioAnual(self):
        return self.sueldo * 3

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}. Sueldo: {self.sueldo} y su premio anual es {self.premioAnual()}"


class Empresa:
    def __init__(self) -> None:
        self.listaEmpleados = []
        e = [("Juan", 100), ("Ana", 200), ("Luis", 300)]
        for x in range(3):
            # nombre = input("Nombre: ")
            # sueldo = int(input("Sueldo: "))
            empleado = Empleado(e[x][0], e[x][1]) # composición
            self.listaEmpleados.append(empleado)

    def getSalarys(self):
        # for empleado in self.listaEmpleados:
        #     print(empleado.nombre, empleado.sueldo)
        return self.listaEmpleados


empresa = Empresa()
for empleado in empresa.getSalarys():
    print(empleado)
