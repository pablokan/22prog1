class Persona:
    especie = "Homo Sapiens"
    def __init__(self, nombre, *args, status="Active") -> None:
        self.nombre = nombre
        self.varios = args
        self.status = status

    def __str__(self) -> str:
        return f"{self.especie}, {self.nombre}, {self.varios}, {self.status}"

juan = Persona("Juan", status="Inactive")
mary = Persona("María", 1,2,3,43)

print(juan)
print(mary)

from dataclasses import dataclass
@dataclass
class Persona2:
    nombre: str
    #varios: tuple
    status: str = "Active"
    especie: str = "Homo Sapiens"

paul = Persona2("Pablo")
print(paul)


@dataclass(init=False)
class ArgHolder:
    args: list[any]

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

a = ArgHolder(1, 2, three=3)
print(a)

@dataclass(frozen=True)
class Fija:
    nombre: str
    edad: int

a = Fija("J", 11)
a.edad = 33
print(a)
