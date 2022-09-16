from dataclasses import dataclass


@dataclass
class Video:
    nombre: str
    visualizaciones: int
    actores: str


@dataclass
class Serie(Video):
    temporadas: int


@dataclass
class Peli(Video):
    duracion: int


class Plataforma:
    def __init__(self) -> None:
        series = [
            [
                "Peaky Blinders",
                1234567,
                "Cillian Murphy,Paul Anderson,Helen McCrory",
                5,
            ],
            [
                "The Umbrella Academy",
                2434908,
                "Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda",
                2,
            ],
        ]

        pelis = [
            [
                "Inception",
                4760183,
                "Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt",
                148,
            ],
            [
                "Batman Begins",
                17319533,
                "Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine",
                140,
            ],
            ["Inmortales", 35, "Mirtha Legrand,Carlitos Balá,Elizabeth The Second", 30],
        ]

        self.listaSeries = []
        for serie in series:
            s = Serie(*serie)
            self.listaSeries.append(s)

        self.listaPelis = [Peli(*p) for p in pelis]

    def masVisto(self):
        # listaV = []
        listaObjetosVideos = self.listaSeries + self.listaPelis
        # for video in listaObjetosVideos:
        #     listaV.append((video.visualizaciones, video.nombre))
        # tuplaMasVista = max(listaV)
        # print(tuplaMasVista[1])

        return max([(v.visualizaciones, v.nombre) for v in listaObjetosVideos])[1]
    
    def promDuracionPelis(self):
        totalMinutos = 0
        for peli in self.listaPelis:
            totalMinutos += peli.duracion
        return totalMinutos//len(self.listaPelis)

    def actoresRepetidos(self):
        actoresSeries = []
        for serie in self.listaSeries:
            actoresSeries += serie.actores.split(",")
        #print(actoresSeries)
        actoresPeliculas = []
        for peli in self.listaPelis:
            actoresPeliculas += peli.actores.split(",")
        #print(actoresPeliculas)
        conjuntoActoresSeries = set(actoresSeries)
        conjuntoActoresPelis = set(actoresPeliculas)
        interseccion = conjuntoActoresPelis.intersection(conjuntoActoresSeries)
        return interseccion

    def seriesMasLargas(self):
        # lista = []
        # print("\nSeries de más de 3 temporadas")
        # for serie in self.listaSeries:
        #     if serie.temporadas > 3:
        #         lista.append(serie.nombre)
        # return lista
        return [serie.nombre for serie in self.listaSeries if serie.temporadas > 3]


netflix = Plataforma()
print(f"Video con mas visualizaciones: {netflix.masVisto()}")
print(f"Promedio de duración de las películas: {netflix.promDuracionPelis()} minutos")
        
print(f"Actores que trabajan en series y también en peliculas: ")
for actor in netflix.actoresRepetidos():
    print(actor)

print("Series con mas de 3 temporadas:")
for serie in netflix.seriesMasLargas():
    print(serie)
