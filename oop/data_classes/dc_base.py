from dataclasses import dataclass, astuple, asdict

@dataclass # decorador: sirve para construir el init y el repr
class Persona:
    nombre: str # atributo: tipo de dato
    edad: int

    # def __str__(self) -> str:
    #     return f"Soy {self.nombre} y tengo {self.edad} años"


# class Persona:
#     def __init__(self, nombre, edad) -> None:
#         self.nombre = nombre
#         self.edad = edad

unaPersona = Persona("Ana", 11)
otraPersona = Persona("José", 22)
print(f"Print del objeto (usa el dunder __repr__): {unaPersona}")
print(f"Print del objeto como tupla: {astuple(unaPersona)}")
print(f"Print del objeto como diccionario: {asdict(unaPersona)}")
