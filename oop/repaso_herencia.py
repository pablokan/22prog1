class Persona:
    def __init__(self, n) -> None:
        self.nombre = n

    def getName(self):
        return self.nombre
    
class Profesor(Persona):
    def __init__(self, n, m) -> None:
        super().__init__(n)
        self.materia = m

class Alumno(Persona):
    def __init__(self, n, p) -> None:
        Persona.__init__(self, n)
        self.promedio = p

docente = Profesor("Pablo", "Matemática")
print(docente.nombre)
print(docente.getName())