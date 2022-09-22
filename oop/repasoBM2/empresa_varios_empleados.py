class Empleado:
    def __init__(self, n, s) -> None: 
        self.nombre = n
        self.sueldo = s 

class Programador(Empleado):
    def __init__(self, n, s, l) -> None: 
        super().__init__(n, s) 
        self.lenguaje = l

    def getSalary(self): 
        return self.sueldo 

    def __str__(self) -> str:
        return f"{self.nombre} - {self.sueldo} - {self.lenguaje}"

class Empresa:
    def __init__(self) -> None:
        self.listaProgramadores = []
        for i in range(2):
            nombre = input("Nombre: ")
            salario = int(input("Salario: "))
            lenguaje = input("Lenguaje: ")
            programador = Programador(nombre, salario, lenguaje)
            self.listaProgramadores.append(programador)
        
    def getDevs(self):
        for prog in self.listaProgramadores:
            print(prog)

microsoft = Empresa()
microsoft.getDevs()
