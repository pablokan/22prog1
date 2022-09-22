from dataclasses import dataclass

@dataclass
class Cancion:
    nombre: str
    duracion: int

    def updDuracion(self, segs):
        print(f"Cambio de duración de {self.nombre}:")
        self.duracion = segs

@dataclass
class Banda:
    nombre: str
    canciones: list

    def addSong(self):
        self.songList = [Cancion(*c) for c in self.canciones]

    def getAll(self, cam, nd):
        for cancion in self.songList:
            print(cancion)
            if cancion.nombre == cam:
                cancion.updDuracion(nd)
                print(cancion)

listaCanciones = [("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)]
zeppelin = Banda("Led Zeppelin", listaCanciones)
zeppelin.addSong()
cancionAmodif = "Black dog"
nuevaDuracion = 321
zeppelin.getAll(cancionAmodif, nuevaDuracion)





