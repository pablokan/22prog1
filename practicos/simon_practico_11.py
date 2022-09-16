
class Video():
    def __init__(self, titulo, visualizaciones, actores):
        self.titulo = titulo        
        self.visualizaciones = visualizaciones
        self.actores = actores

    def mayorVisualizacion(self):
        self.aux = -1
        self.videoMasVisto = ""
        for pelicula in listaObjPeliculas:
            if pelicula.visualizaciones > self.aux:
                self.aux = pelicula.visualizaciones
                self.videoMasVisto = pelicula.titulo
                tipo = "pelicula"
        for serie in listaObjSeries:
            if serie.visualizaciones > self.aux:
                self.aux = serie.visualizaciones
                self.videoMasVisto = serie.titulo
                tipo = "serie"
        return f"El video con mas visualizaciones es la {tipo} {self.videoMasVisto} con {self.aux} reproducciones"

    def actoresMixtos(self):
        listaActoresSerie = []
        listaActoresPelicula = []
        for serie in listaObjSeries:
            lA = serie.actores.split(",")
            for actor in lA:
                listaActoresSerie.append(actor)

        for pelicula in listaObjPeliculas:
            lA = pelicula.actores.split(",")
            for actor in lA:
                listaActoresPelicula.append(actor)

        for actorSerie in listaActoresSerie:
            for actorPelicula in listaActoresPelicula:
                if actorSerie == actorPelicula:
                    print(f"{actorSerie} trabajó en series y peliculas")
        

    

class Pelicula(Video):
    def __init__(self, titulo, visualizaciones, actores, duracion):
        super().__init__(titulo, visualizaciones, actores)
        self.duracion = duracion

    def promedioDuracion(self):
        self.suma = 0
        for pelicula in listaObjPeliculas:
            self.suma += pelicula.duracion
        return f"El promedio de duracion de las peliculas es de {self.suma/len(listaObjPeliculas)} minutos"



class Serie(Video):
    def __init__(self, titulo, visualizaciones, actores, temporadas):
        super().__init__(titulo,visualizaciones,actores)
        self.temporadas = temporadas

    def serieMas3Temporadas(self):
        for serie in listaObjSeries:
            if serie.temporadas > 3:
                return f"{serie.titulo} tiene mas de 3 temporadas ({serie.temporadas})"

class Netflix():
    def __init__(self,tipo):
        self.listaPeliculasNetflix = []
        self.listaSeriesNetflix = []
        if tipo.upper() == "PELICULA":
            preg = "si"
            while preg.upper() == "SI":
                actores = ""
                titulo = input(f"Ingrese el titulo de la pelicula: ")
                visualizaciones = int(input(f"Cuantas visualizaciones tiene? "))
                nA = int(input(f"Cuantos actores/actrices tiene? "))
                for i in range(nA):
                    actor = input(f"Ingrese el nombre del actor/actriz #{i+1}: ")
                    actores += actor + ","
                actores = actores[:-1]
                duracion = int(input(f"Ingrese la duracion de la pelicula en minutos: "))
                pelicula = Pelicula(titulo,visualizaciones,actores,duracion)
                self.listaPeliculasNetflix.append(pelicula)
                preg = input(f"Desea agregar otra pelicula? ")
        if tipo.upper() == "SERIE":
            preg = "si"
            while preg.upper() == "SI":
                actores = ""
                titulo = input(f"Ingrese el titulo de la serie: ")
                visualizaciones = int(input(f"Cuantas visualizaciones tiene? "))
                nA = int(input(f"Cuantos actores/actrices tiene? "))
                for i in range(nA):
                    actor = input(f"Ingrese el nombre del actor/actriz #{i+1}: ")
                    actores += actor + ","
                actores = actores[:-1]
                temporadas = int(input(f"Ingrese la cantidad de temporadas: "))
                serie = Serie(titulo,visualizaciones,actores,temporadas)
                self.listaSeriesNetflix.append(serie)
                preg = input(f"Desea agregar otra serie? ")
    def getInformacionPeliculas(self):
        for pelicula in self.listaPeliculasNetflix:
            print(f"Titulo: {pelicula.titulo}. Visualizaciones: {pelicula.visualizaciones}. Actores: {pelicula.actores}. Duracion: {pelicula.duracion}min")
                
    def getInformacionSeries(self):
        for serie in self.listaSeriesNetflix:
            print(f"Titulo: {serie.titulo}. Visualizaciones: {serie.visualizaciones}. Actores: {serie.actores}. Temporadas: {serie.temporadas}")
    



series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 5],
["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 2]]

pelis = [["Inception", 4760183, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148],
["Batman Begins", 17319533, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140],       
["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30]]

listaObjSeries = []
listaObjPeliculas = []

for serie in series:
    titulo = serie[0]
    visualizaciones = serie[1]
    actores = serie[2]
    temporadas = serie[3]
    objSerie = Serie(titulo,visualizaciones,actores,temporadas)
    listaObjSeries.append(objSerie)

for pelicula in pelis:
    titulo = pelicula[0]
    visualizaciones = pelicula[1]
    actores = pelicula[2]
    duracion = pelicula[3]
    objPelicula = Pelicula(titulo,visualizaciones,actores,duracion)
    listaObjPeliculas.append(objPelicula)


print(objPelicula.mayorVisualizacion())
print(objPelicula.promedioDuracion())
print(objSerie.serieMas3Temporadas())
objSerie.actoresMixtos()

