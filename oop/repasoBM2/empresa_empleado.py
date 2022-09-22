class Empleado:
    def __init__(self, n, s) -> None: # Paso 3 de los 230 mil
        self.nombre = n
        self.sueldo = s # Paso 4 de los 230 mil

class Programador(Empleado):
    def __init__(self, n, s, l) -> None: # Paso 1 de los 230 mil
        super().__init__(n, s) # Paso 2 de los 230 mil
        self.lenguaje = l

    def getSalary(self): #self representa el objeto de la clase donde estoy
        # self.sueldo === josefa.sueldo
        return self.sueldo # # Paso 5 de los 230 mil: el sueldo de Josefa

class Empresa:
    def __init__(self) -> None:
        self.josefa = Programador("Josefa", 230_000, "PHP") # adonde van los 230 mil?

    def getSalary(self):
        # self.sueldo === Google.sueldo (que NO existe)
        #return self.sueldo # NO es válido
        return self.josefa.sueldo # Google.josefa.sueldo

Google = Empresa()
print(Google.josefa.sueldo)
print(Google.getSalary())
