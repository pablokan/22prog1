# Composición propiamente dicha
# clase dependiente DEBE ser obligatoriamente instanciada

class Puerta():
    def __init__(self, uv, uh) -> None:
        self.uv = uv
        self.uh = uh

    def abrirPuerta(self):
        print(f"Abierta la puerta {self.uv} {self.uh}")
        
    def cerrarPuerta(self):
        print(f"Cerrada la puerta {self.uv} {self.uh}")

class Auto():
    def __init__(self, tipoAuto, nombre) -> None:
        # Composición
        print(nombre, end=": ")
        self.di = Puerta("delantera", "izquierda") # agrega una puerta
        self.dd = Puerta("delantera", "derecha") # agrega otra puerta
        if tipoAuto == "sedán":
            self.ti = Puerta("trasera", "izquierda")
            self.td = Puerta("trasera", "derecha")

cupecita = Auto("cupé", "Cupecita")
cupecita.di.abrirPuerta()
cupecita.di.cerrarPuerta()
duna = Auto("sedán", "Duna")
duna.td.abrirPuerta()

