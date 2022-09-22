class Persona():
    def __init__(self, n, e, s) -> None:
        self.nombre = n
        self.edad = e
        self.sexo = s

    def mayorEdad(self):
        if self.edad >= 18:
            return "mayor de edad"
        else:
            return "menor de edad"

    def varonOmujer(self):
        if self.sexo == "m":
            return "varón"
        else:
            return "mujer"

    def __str__(self) -> str:
      return f"{self.nombre} es {self.mayorEdad()} y es {self.varonOmujer()}"  


persona = Persona("Juan", 32, "m")
print(persona)
otraPersona = Persona("Ana", 11, "f")
print(otraPersona)
