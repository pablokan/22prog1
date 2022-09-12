from dataclasses import dataclass

@dataclass
class Deportista:
    nombre: str
    altura: float = 0
    peso: float = 0

    def __str__(self) -> str:
        return f'{self.nombre}: {self.altura}, {self.peso}'

@dataclass
class Equipo(Deportista):
    equipo: str = 'desconocido'

    def __str__(self) -> str:
        return f'{self.nombre}: {self.equipo}'

# Instancia la clase Deportista para crear objeto:
deportista1 = Deportista('Elena', 1.81, 64)

# Imprime llamando al método __str__() de
# la clase Deportista:
print(deportista1)  # Elena: 1.81, 64

# Instancia la clase Equipo para crear objeto:
deportista2 = Equipo('Marta', equipo='Sevilla')

# Imprime llamando al método __str__() de
# la clase Equipo:
print(deportista2)  # Marta: Sevilla

# Asigna valores a atributos de objeto de la clase Equipo:
deportista2.altura = 1.76
deportista2.peso = 68

# Imprime representación formal de objeto de la clase Equipo:
print(repr(deportista2))

# Equipo(nombre='Marta', altura=1.76, peso=68, equipo='Sevilla')