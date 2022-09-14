from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int

unaPersona = Persona("Ana", 11)
print(unaPersona)
