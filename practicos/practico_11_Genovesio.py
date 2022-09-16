from dataclasses import dataclass


@dataclass
class Obras:
    nombre: str
    visualizaciones: int
    actores: str

    def vistas(self):
        return self.visualizaciones
    
    def elenco(self):
        return self.actores.split(",")
    
    def tiempo(self):
        pass

@dataclass
class Pelicula(Obras):
    duracion: int

    def tiempo(self):
        return self.duracion

@dataclass   
class Serie(Obras):
    temporadas: int
    
    def tiempo(self):
        if self.temporadas >= 3:
            return True
        else:
            return False

peliculas = [Pelicula ("Inception", 4760183, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148),
             Pelicula ("Batman Begins", 17319533, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140),       
             Pelicula ("Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30)]

series = [Serie("Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 5),
          Serie("The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 2)]

def mas_visto(pelis, series):
    mayor = 0
    nombre = ""
    tipo = ""
    for elemento in pelis:
        if elemento.vistas() > mayor:
            mayor = elemento.vistas()
            nombre = elemento.nombre
            tipo = "pelicula"
    for elemento in series:
        if elemento.vistas() > mayor:
            mayor = elemento.vistas()
            nombre = elemento.nombre
            tipo = "serie"

    return f"la {tipo} que mas visualizaciones tiene es {nombre} con {mayor} vistas"

def promedio_peliculas(pelis):
    total = 0
    for elemento in pelis:
        total += elemento.tiempo()

    total = total / len(pelis)

    return f"el promedio de duracion de las peliculas es de: {total} minutos"

def nombres_repetidos(pelis, series):
    lista_pelis = []
    lista_series = []
    for elemento in pelis:
        for persona in elemento.elenco():
            if persona not in lista_pelis:
                lista_pelis.append(persona)


    for elemento in series:
        for persona in elemento.elenco():
            if persona not in lista_series:
                lista_series.append(persona)

    print("las personas repetidas son:")
    for persona in lista_pelis:
        if persona in lista_series:
            print(f"  -{persona} ")

    return ""

def series_largas(series):
    print("las series con mas de 3 temporadas son:")
    for elemento in series:
        if elemento.tiempo() == True:
            print(f"    -{elemento.nombre}")
    
    return ""

print(f"\n{mas_visto(peliculas,series)}\n")
print(f"{promedio_peliculas(peliculas)}\n")
print(nombres_repetidos(peliculas,series))
print(series_largas(series))