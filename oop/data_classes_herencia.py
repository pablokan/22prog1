from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int

@dataclass
class Profesor(Persona):
    materia: str

prof = Profesor("Juan", 44, "Matemática")
print(prof)

