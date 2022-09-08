class Algo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def __str__(self) -> str:
        return f"Mi nombre es {self.nombre}"


print(Algo("José"))