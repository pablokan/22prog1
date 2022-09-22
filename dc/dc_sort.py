from dataclasses import dataclass, field


@dataclass(order=True)
class Persona:
    #sort_index: int = field(init=False, repr=False)
    name: str
    age: int

    # def __post_init__(self):
    #     self.sort_index = self.age


personas = [
    Persona("Ana", 44),
    Persona("Juan", 58),
    Persona("Beto", 32)
]

print(sorted(personas))



