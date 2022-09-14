from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int
    
@dataclass
class Profesor(Persona):
    materia: str

profe = Profesor("Beto", 33, "Lengua")
print(profe)

