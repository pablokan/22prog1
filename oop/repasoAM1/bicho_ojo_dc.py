from dataclasses import dataclass

@dataclass
class Ojo:
    color: str

@dataclass
class Bicho:
    peso: int

    def __post_init__(self):
        self.ojo = Ojo("rojo")

cucaracha = Bicho(10)
print(cucaracha.ojo.color)
