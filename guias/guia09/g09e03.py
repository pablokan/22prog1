class Motor:
    def arrancar(self):
        print("Arrancó!")

    def apagar(self):
        print("Motor apagado")

class Rueda:
    def inflar(self):
        print("Rueda inflada")

    def desinflar(self):
        print("Rueda desinflada")

class Puerta:
    def abrir(self):
        print("Puerta abierta")

    def cerrar(self):
        print("Puerta cerrada")

class Auto:
    motor = Motor()
    puertaIzquierda = Puerta()
    puertaDerecha = Puerta()
    rueda1 = Rueda()
    rueda2 = Rueda()
    rueda3 = Rueda()
    rueda4 = Rueda()

auto = Auto()
auto.puertaDerecha.abrir()
