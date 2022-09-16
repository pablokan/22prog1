from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int
    mayor: bool = False

    def __post_init__(self):
        if self.edad >= 18:
            self.mayor = True

unaPersona = Persona("Ana", 11)
print(unaPersona)
otraPersona = Persona("José", 22)
print(otraPersona)
