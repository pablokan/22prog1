from dataclasses import dataclass

@dataclass
class Ojo:
    color: str

@dataclass
class Bicho:
    peso: int
    ojo = Ojo("rojo")

cucaracha = Bicho(10)
print(cucaracha.ojo.color)
