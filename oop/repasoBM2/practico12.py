from dataclasses import dataclass

@dataclass
class Empleado:
    nombre: str
    sueldo: int

@dataclass
class Programador(Empleado):
    lenguaje: str

    def setProject(self, project):
        self.proyecto = project

    def getProjAndLang(self):
        return f"Sistema: {self.proyecto}. Lenguaje: {self.lenguaje}"

@dataclass
class Empresa:
    nombre: str
    rubro: str
    listaProyectos = ["Pollitos", "Gallinas"]
    listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
    listaProgramadores = []

    def getName(self):
        return f"Empresa: {self.nombre}"

    def getRubro(self):
        return f"Rubro: {self.rubro}"

    def agEmp(self):
        lenguaje = input("Lenguaje: ")
        if lenguaje in self.listaLenguajes:
            # Opciones de instanciación posibles con datos incompletos
            # p = Programador(None, None, lenguaje)

            # p = Programador("", 0, lenguaje)
            # nombre = input("Nombre: ")
            # p.nombre = nombre
            
            nombre = input("Nombre: ")            
            if lenguaje == "Python":
                sueldo = 475_000
            else:
                sueldo = 215_000
            p = Programador(nombre, sueldo, lenguaje)
            proyecto = input(f"Elija un proyecto: {self.listaProyectos}")
            p.setProject(proyecto)
            self.listaProgramadores.append(p)

        else:
            print("El lenguaje ingresado no se requiere.")
            print("Los lenguajes requeridos son:", self.listaLenguajes)

    def mostrarTodo(self):
        print(f"Empresa: {self.nombre}. {self.getRubro()}")
        print("Programadores:")
        # Pedro. Salario: 215000. Sistema: Gallina SRL. Lenguaje: C#
        for p in self.listaProgramadores:
            #print(f"{p.nombre}. Salario: {p.sueldo}. Sistema: {p.proyecto}. Lenguaje: {p.lenguaje}")
            print(f"{p.nombre}. Salario: {p.sueldo}. {p.getProjAndLang()}")

twitter = Empresa("Twitter", "Red Social")
for _ in range(4):
    twitter.agEmp()
twitter.mostrarTodo()
