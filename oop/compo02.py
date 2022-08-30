# Agregación: es cuando la clase subsidiaria puede o no ser instanciada
# En términos de implementación, no se distingue de la composición normal

class Empleado():
    def __init__(self, n) -> None:
        self.nombre = n

    def getName(self):
        return self.nombre

class Empresa():
    def __init__(self) -> None:
        self.le = []
        for x in range(3):
            nombre = input("Nombre: ")
            e = Empleado(nombre) # agregación o composición
            self.le.append(e)

    def listarEmpleados(self):
        return self.le


empresa = Empresa()
for empleado in empresa.listarEmpleados():
    print(empleado.getName())
