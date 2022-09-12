from dataclasses import dataclass, field

@dataclass
class Deportista:
    nombre: str
    altura: float
    peso: float = field(init=False, repr=False)

deportista1 = Deportista('Elena', 1.81)
deportista1.peso = 64
print(deportista1)  # Deportista(nombre='Elena', altura=1.81)
print(deportista1.peso)  # 64
