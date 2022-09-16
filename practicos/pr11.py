# start time: 17:59
# end time: 18:44

from dataclasses import dataclass


@dataclass
class Video:
    nombre: str
    visualizaciones: int
    actores: list[str]


@dataclass
class Serie(Video):
    temporadas: int


@dataclass
class Peli(Video):
    duracion: int


@dataclass
class Netflix:
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
            [
                "Inmortales",
                35,
                "Mirtha Legrand,Carlitos Balá,Elizabeth The Second",
                30,
            ],
        ]

        self.listaSeries = listaSeries = []
        for serie in series:
            s = Serie(*serie)
            listaSeries.append(s)

        self.listaPelis = listaPelis = []
        for peli in pelis:
            p = Peli(*peli)
            listaPelis.append(p)

    def masVisto(self):
        return max(
            [(v.visualizaciones, v.nombre) for v in self.listaSeries + self.listaPelis]
        )[1]

    def promDurPel(self):
        return sum([p.duracion for p in self.listaPelis])/len(self.listaPelis)

    def actoresSeriesPelis(self):
        def getSet(listaVideos):
            listaActores = []
            for v in listaVideos:
                listaActores += v.actores.split(",")
            return set(listaActores)

        conjuntoActoresSeries = getSet(self.listaSeries)
        conjuntoActoresPelis = getSet(self.listaPelis)

        interseccion = conjuntoActoresPelis.intersection(conjuntoActoresSeries)
        for actor in interseccion:
            print(actor)

    def seriesMasLargas(self):
        for s in self.listaSeries:
            if s.temporadas > 3:
                print(s.nombre)


netflix = Netflix()
print(netflix.masVisto())
print(netflix.promDurPel())
netflix.actoresSeriesPelis()
netflix.seriesMasLargas()