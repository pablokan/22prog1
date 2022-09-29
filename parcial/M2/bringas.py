
from dataclasses import dataclass

@dataclass
class Banda:
    nombreBnada=str

@dataclass
class Canciones (Banda):
    nombreCancion = str
    duracion= int
    listaCanciones = [("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)]
    cancion1 = listaCanciones[1][0]
    print(cancion1)
    duracion1=listaCanciones[0][1]
    print(duracion1)
    
    cancion2= listaCanciones[0][1]
    print(cancion2)
    duracion2= listaCanciones[1][1]
    print(duracion2)

    cancion3= listaCanciones[2][0]
    print(cancion3)
    duracion3=listaCanciones[2][1]
    print(duracion3)


    def modificacionDuracion (self, duracion):
        self.duracion= duracion 
        print(f"La cancion que se modifica es {self.nombreCancion}")

    def MostrarCambiosDuracion (self):
        return f"El cambio de la duracion es de: {self.modificacionDuracion}"

nombreBanda = [("Led Zeppelin")]
listaCanciones = [("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)]
     





