from dataclasses import dataclass

@dataclass
class Empleado:
    nombre: str
    sueldo: int

@dataclass
class Programador(Empleado):
    lenguaje: str

    def getSalary(self):
        return self.sueldo

@dataclass
class Empresa:
    josefa = Programador("Josefa", 230_000, "PHP") # adonde van los 230 mil?

    def getSalary(self):
        return self.josefa.sueldo

Google = Empresa()
print(Google.josefa)
print(Google.getSalary())




