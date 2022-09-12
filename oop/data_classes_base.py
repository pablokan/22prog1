from dataclasses import dataclass, astuple, asdict

@dataclass # decorador: me permite hacer una declaración especial
class Persona:
    nombre: str # atributo: tipo_de_dato
    edad: int
    estado: str = "Activo"

    def __str__(self) -> str:
        return f"Soy {self.nombre} y tengo {self.edad} años"
        
# class Persona:
#     def __init__(self, nombre, edad, estado="Activo") -> None:
#         self.nombre = nombre
#         self.edad = edad

unaPersona = Persona("Ana", 11)
otraPersona = Persona("José", 22)
print("Print en formato __str__:", unaPersona)
print("Print en formato tupla:", astuple(unaPersona))
print("Print en formato diccionario:", asdict(unaPersona))
print("Print en formato __repr__:", otraPersona.__repr__())


