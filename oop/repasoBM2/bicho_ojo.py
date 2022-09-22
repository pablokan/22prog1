class Ojo:
    def __init__(self, c) -> None:
        self.color = c

class Bicho:
    def __init__(self) -> None:
        self.ojo = Ojo("azul") # composición 

mosca = Bicho()
print(mosca.ojo.color)
# objeto de la clase principal.su atributo (que también es un objeto). atributo del obj de la clase secundaria
