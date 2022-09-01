class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Profesor(Persona):
    def __init__(self, nombre, materia) -> None:
        Persona.__init__(self, nombre) # si usa el nombre de la clase madre hay que poner self como parámetro
        self.materia = materia

class Alumno(Persona):
    def __init__(self, nombre, promedio) -> None:
        super().__init__(nombre) # si usa super no pone self
        self.promedio = promedio

docente1 = Profesor("Pedro", "Inglés")
alumno1 = Alumno("Cintia Red", 9.87)

print(docente1.nombre)
print(alumno1.nombre)
