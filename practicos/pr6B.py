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

def pelisXgenero(genero):
    print(f"Películas de {genre[g]}")
    for movie in movies:
        if genero in movie:
            posParentesis = movie.find("(")
            nombre = movie[:posParentesis]
            print(f"- {nombre}")

def cantidadDePelisAnterioresAl(anioTope):
    c = 0
    for movie in movies:
        posParentesis = movie.find("(")
        aEstreno = int(movie[posParentesis+1:posParentesis+5])
        if aEstreno < anioTope:
            c += 1
    print(f"La cantidad de pelis anteriores al año {anioTope} son {c}")

def pelisXinicial(inicial):
    for movie in movies:
        if inicial == movie[0]:
            posParentesis = movie.find("(")
            nombre = movie[:posParentesis]
            aEstreno = int(movie[posParentesis+1:posParentesis+5])
            genero = genre[movie[posParentesis+6:]]
            print(f"{nombre}. Año: {aEstreno}. Género: {genero}")


g = input("Ingrese un género: ")
pelisXgenero(g)
a = int(input("Ingrese año tope: "))
cantidadDePelisAnterioresAl(a)
i = input("Ingrese inicial: ")
pelisXinicial(i)
