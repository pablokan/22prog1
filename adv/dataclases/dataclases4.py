from dataclasses import dataclass, asdict

@dataclass
class Deportista:
    nombre: str
    altura: float
    peso: float

deportista1 = Deportista('Elena', 1.81, 64)
dicc1 = asdict(deportista1)

if dicc1['altura'] > 1.75:
   print(dicc1['nombre'], 'supera la altura')