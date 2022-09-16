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


class Netflix:
    def __init__(self) -> None:
        series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 5],
                  ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 2]]

        pelis = [["Inception", 4760183, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148],
                 ["Batman Begins", 17319533,
                     'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140],
                 ["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30]]

        # ZacaStyle
        self.listaSeries = [Serie(*serie) for serie in series] 

        self.listaPelis = []
        for peli in pelis:
            p = Peli(*peli)
            self.listaPelis.append(p)
       
    def masVisto(self):
        lista = []
        for video in self.listaSeries + self.listaPelis:
            tupla = (video.visualizaciones, video.nombre)
            # cada tupla es tipo (12324225525, "Inception")
            lista.append(tupla) # lista de tuplas
        visual, nombrePeli = max(lista) # (17319533, "Batman begins")
        salida = f"El video mas visto es {nombrePeli} y fue vista {visual} veces"
        return salida

        # ZacaStyle
        #return max(
        #     [(v.visualizaciones, v.nombre) for v in self.listaSeries + self.listaPelis]
        # )[1]

    def promPelis(self):
        cantMinutos = 0
        for peli in self.listaPelis:
            cantMinutos += peli.duracion
        return cantMinutos // len(self.listaPelis)

    def actoresDoble(self):
        actoresSeries = []
        for serie in self.listaSeries:
            lista = serie.actores.split(",")
            actoresSeries += lista

        print(actoresSeries)

        actoresPelis = []
        for peli in self.listaPelis:
            lista = peli.actores.split(",")
            actoresPelis += lista

        print(actoresPelis)

        for aS in actoresSeries:
            for aP in actoresPelis:
                if aS == aP:
                    print(aS) 

    def actoresRepetidos(self):
        actoresSeries = []
        for serie in self.listaSeries:
            lista = serie.actores.split(",")
            actoresSeries += lista
        actoresPelis = []
        for peli in self.listaPelis:
            lista = peli.actores.split(",")
            actoresPelis += lista

        actoresSeries = set(actoresSeries)
        actoresPelis = set(actoresPelis)

        for a in actoresPelis.intersection(actoresSeries):
            print(a)
    
    def seriesMasLargas(self):
        for s in self.listaSeries:
            if s.temporadas > 3:
                print(s.nombre)

netflix = Netflix()
print(netflix.masVisto())
print(netflix.promPelis())
netflix.actoresDoble()
netflix.actoresRepetidos()
netflix.seriesMasLargas()