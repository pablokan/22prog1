from dataclasses import dataclass

@dataclass
class Usuario:
    id: int
    name: str

u1 = Usuario(id=1, name='Juan')
u2 = Usuario(id=2, name='Juan')

print(u1.name)
if u1 > u2:
    print('mayor')