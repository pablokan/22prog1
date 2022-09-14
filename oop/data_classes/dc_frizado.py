from dataclasses import dataclass

@dataclass(frozen=True) # no se puede modificar los atributos luego de la inicialización
class Persona:
    nombre: str
    edad: int

unaPersona = Persona("Ana", 11)
unaPersona.edad = 13
print(unaPersona)
otraPersona = Persona("José", 22)