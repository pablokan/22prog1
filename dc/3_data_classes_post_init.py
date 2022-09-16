from dataclasses import dataclass, field

@dataclass
class Persona:
    nombre: str
    edad: int
    mayor: bool = None

    def __post_init__(self): # se ejecuta automática luego del constructor
        if self.edad >= 18:
            self.mayor = True

p = Persona("Juan", 22)
print(p)
