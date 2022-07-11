movies = [
    "Das boot(1981)act",
    "Blade Runner(1982)sf",
    "Arrival(2016)sf",
    "Dumb & Dumber(1994)com",
    "Blade Runner 2049(2015)sf",
    "Three Kings(1999)act",
    "The green hornet(2011)com",
]
genre = {"act": "Acción", "sf": "Ciencia Ficción", "com": "Comedia"}
nombres = []
anios = []
generos = []

def separarDatos():
    for movie in movies:
        posParentesis = movie.find("(")
        nombre = movie[:posParentesis]
        nombres.append(nombre)
        aEstreno = int(movie[posParentesis+1:posParentesis+5])
        anios.append(aEstreno)
        genero = movie[posParentesis+6:]
        generos.append(genero)

def pelisXgenero(genero):
    print(f"Películas de {genre[g]}")
    for i in range(len(generos)):
        if genero == generos[i]:
            print(f"- {nombres[i]}")

def cantidadDePelisAnterioresAl(anioTope):
    c = 0
    for aEstreno in anios:
        if aEstreno < anioTope:
            c += 1
    print(f"La cantidad de pelis anteriores al año {anioTope} son {c}")

def pelisXinicial(inicial):
    for i in range(len(movies)):
        if inicial == movies[i][0]:
            print(f"{nombres[i]}. Año: {anios[i]}. Género: {genre[generos[i]]}")

separarDatos()
g = input("Ingrese un género: ")
pelisXgenero(g)
a = int(input("Ingrese año tope: "))
cantidadDePelisAnterioresAl(a)
i = input("Ingrese inicial: ")
pelisXinicial(i)
