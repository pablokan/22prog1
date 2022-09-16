from dataclasses import dataclass, field

@dataclass(order=True)
class P:
    orden: any = field(init=False, repr=False) # NO va en el constructor ni en el repr. any es cualquier tipo de dato
    nombre: str
    edad: int
    altura: float

    def __post_init__(self):
        self.orden = self.edad # pongo la edad en el campo orden para que ordene por edad

personas = [P("Beto", 33, 1.77), P("Ana", 11, 1.80), P("José", 22, 1.55)]
print(personas)
print(sorted(personas, reverse=True))


