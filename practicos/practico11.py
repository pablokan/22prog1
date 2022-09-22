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
        series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 5],
                    ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 2]]

        pelis = [["Inception", 4760183, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148],
                    ["Batman Begins", 17319533, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140],       
                    ["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30]]
	

        self.listaSeries = []
        for serie in series:
            s = Serie(*serie)
            self.listaSeries.append(s)
    
        self.listaPelis = [Peli(*peli) for peli in pelis]

    def masVisto(self):
        # todos = self.listaSeries + self.listaPelis
        # listaVis = []
        # for video in todos:
        #     listaVis.append((video.visualizaciones, video.nombre))
        # print(max(listaVis)[1])
        print(max([(v.visualizaciones, v.nombre) for v in self.listaSeries + self.listaPelis])[1])

    def promDuracionPelis(self):
        minutos = 0
        for peli in self.listaPelis:
            minutos += peli.duracion
        print(minutos//len(self.listaPelis))

    def actoresRepetidos(self):
        actoresSeries = []
        for serie in self.listaSeries:
            serieActores = serie.actores.split(",")
            actoresSeries += serieActores
        #print(actoresSeries)

        actoresPelis = []
        for peli in self.listaPelis:
            peliActores = peli.actores.split(",")
            actoresPelis += peliActores
        #print(actoresPelis)
        print(set(actoresSeries).intersection(set(actoresPelis)))

    def seriesMasLargas(self):
        for serie in self.listaSeries:
            if serie.temporadas > 3:
                print(serie.nombre)

netflix = Plataforma()
netflix.masVisto()
netflix.promDuracionPelis()
netflix.actoresRepetidos()
netflix.seriesMasLargas()
