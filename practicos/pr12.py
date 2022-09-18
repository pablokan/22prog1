from dataclasses import dataclass

@dataclass
class Empleado:
    nombre: str
    sueldo: float

@dataclass
class Programador(Empleado):
    lenguaje: str

    def setProyecto(self, proy):
        self.proyecto = proy

    def getData(self):
        return self.proyecto, self.lenguaje

@dataclass
class Empresa:
    nombre: str
    rubro: str

    def __post_init__(self) -> None:
        self.listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
        self.listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
        self.listaProgramadores = []

    def getData(self):
        return self.nombre, self.rubro

    def agEmp(self):
        for x in range(4):
            lenguaje = input("Lenguaje: ")
            if lenguaje in self.listaLenguajes:
                nombre = input("Nombre: ")
                salario = 475_000 if lenguaje == "Python" else 215_000
                d = {}
                for i, p in enumerate(self.listaProyectos, 1):
                    print(i, p)
                    d[i] = p
                
                op = int(input("Elija proyecto: "))
                programador = Programador(nombre, salario, lenguaje)
                programador.setProyecto(d[op])
                self.listaProgramadores.append(programador)

    def mostrarTodo(self):
        print(self.getData())
        for p in self.listaProgramadores:
            print(p.nombre, p.sueldo, p.proyecto, p.lenguaje)

empresa = Empresa("Google", "Informática")
empresa.agEmp()
empresa.mostrarTodo()

