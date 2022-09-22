class Ojo:
    def __init__(self, c) -> None:
        self.color = c

class Bicho:
    def __init__(self, p) -> None:
        self.peso = p
        self.ojo = Ojo("azul") # composición

    def mostrarColorOjos(self):
        return self.ojo.color


cucaracha = Bicho(10)
print(cucaracha.ojo.color) 
# cucaracha: objeto de la clase principal
# ojo: objeto de la clase componente <-> atributo del objeto de la clase principal
# color: atributo de la clase componente o secundaria
print(cucaracha.mostrarColorOjos())