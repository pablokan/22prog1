class Banda:
    NombreBand = str()
    def __init__(self,NombreBand):
        self.NombreBanda = NombreBand

    def IniciarAPP(self):
        listaCanciones =   [("The rain song", 452), 
                            ("Black dog", 296), 
                            ("Kashmir", 512)]
        print(f"Nombre de la banda: {self.NombreBanda}\n")
        print(Cancion(listaCanciones[0][0],listaCanciones[0][1]))
        Dato2 = Cancion(listaCanciones[1][0],listaCanciones[1][1])
        print(Dato2)
        Dato2.ModificarDuracionCancion(321)
        print(Dato2)
        print(Cancion(listaCanciones[2][0],listaCanciones[2][1]))

class Cancion:
    NombCan = str()
    DuracCan = int()
    def __init__(self,NombCan,DuracCan):
        self.NombreCancion = NombCan
        self.DuraccionCancion = DuracCan

    def ModificarDuracionCancion(self,DuraccionNueva):
        print(f"Cambio de Duracion de {self.NombreCancion}")
        self.DuraccionCancion = DuraccionNueva

    def __str__(self):
        return f"Nombre Cancion: {self.NombreCancion}, Duracion: {self.DuraccionCancion}"

nombreBanda = "LedZeppelin"
Dato1 = Banda(nombreBanda)
Dato1.IniciarAPP()