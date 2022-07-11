from json import loads
import json

from menu_creator import menu

def jsonTOcsv():
    def quitarComas(string):
        return string.replace(',', '')

    peliArchJson = open("practicos/pelis.json", "r")
    d = loads(peliArchJson.read())

    peliArchCSV = open("practicos/pelis.csv", "w")

    for peli in d:
        pelicula = peli["Title"]
        protagonista = peli["Actors"].split(",")[0]
        rating = peli["Ratings"][1]["Value"][:-1]
        recaudacion = quitarComas(peli["BoxOffice"][1:])
        linea = f'{pelicula},{protagonista},{rating},{recaudacion}\n'
        peliArchCSV.write(linea)

    peliArchJson.close()
    peliArchCSV.close()

def datosObtenidos():
    peliArchCSV = open("practicos/pelis.csv", "r")
    lineas = peliArchCSV.readlines()
    peliArchCSV.close()
    sumaRating = 0
    sumaRecaudacion = 0
    for linea in lineas:
        linea = linea.split(",")
        sumaRating += int(linea[2])
        sumaRecaudacion += int(linea[3][:-1])
    promedioRating = sumaRating // len(lineas)
    print(f"El promedio de rating es {promedioRating}")
    print(f"La suma de recaudaciones es {sumaRecaudacion}")

jsonTOcsv()
datosObtenidos()

