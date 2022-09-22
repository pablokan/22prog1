from dataclasses import dataclass

@dataclass
class Empleado:
    nombre: str
    sueldo: int

@dataclass
class Programador(Empleado):
    lenguaje: str
    # def __init__(self, lenguaje):
    #     super().__init__(nombre, sueldo)
    #     self.lenguaje = lenguaje

    def asignarProyecto(self, proyecto):
        self.proyecto = proyecto

    def getProyLeng(self):
        return f"Sistema: {self.proyecto}. Lenguaje: {self.lenguaje}"

class Empresa: # composición de Programadores
    def __init__(self, nombre, rubro) -> None:
        self.nombre = nombre
        self.rubro = rubro
        self.listaProyectos = ["Pollitos", "Gallinas"]
        self.listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
        self.listaProgramadores = []

    def agEmp(self):
        lenguaje = input("Que lenguaje sabe? ")
        if lenguaje in self.listaLenguajes:
            nombre = input("Ingrese su nombre: ")
            if lenguaje == "Python":
                sueldo = 475_000
            else:
                sueldo = 215_000
            programador = Programador(nombre, sueldo, lenguaje)
            print(self.listaProyectos)
            proyecto = input("Escriba el nombre del proyecto elegido: ")
            programador.asignarProyecto(proyecto)
            self.listaProgramadores.append(programador)
        else:
            print(f"El lenguaje {lenguaje} no es requerido por esta empresa")

    def mostrarTodo(self):
        print(f"Empresa {self.nombre}. Rubro {self.rubro}")
        print("Programadores:")
        for p in self.listaProgramadores:
            #print(f"{p.nombre}. Salario: {p.sueldo}. Sistema: {p.proyecto}. Lenguaje: {p.lenguaje}")
            print(f"{p.nombre}. Salario: {p.sueldo}. {p.getProyLeng()}")
    
empresa = Empresa("iTecLABS", "Desarrollo de Software")
for x in range(4):
    empresa.agEmp() 
empresa.mostrarTodo()


