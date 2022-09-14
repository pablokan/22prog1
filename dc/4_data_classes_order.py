from dataclasses import dataclass, field


@dataclass(order=True) # por defecto ordena por el primer atributo
class Persona:
    # este atributo indice es para ordenar solamente
    # init=False: es para que no vaya en el constructor
    # repr=False: es para que no salga en el print
    indice: int = field(init=False, repr=False)
    nombre: str
    edad: int

    def __post_init__(self): # se ejecuta automática luego del constructor
        self.indice = self.edad

personas = [Persona("Juan", 222), Persona("Vilma", 33), Persona("Beto", 11)]

for personaOrdenada in sorted(personas):
    print(personaOrdenada)

