from dataclasses import dataclass

@dataclass(frozen=True) # solamente puedo pasar argumentos en el constructor
class Persona:
    nombre: str
    edad: int

    def setNombre(self, n):
        self.nombre = n

persona = Persona("Juan", 22)
print(persona)
persona.setNombre("José") # le cambio el nombre, si está frizado da error
persona.edad = 123 # tampoco va a funcionar
print(persona)





