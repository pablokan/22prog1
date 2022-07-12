from json import loads

# Apertura del archivo de texto JSON
archivoPelisJSON = open("repaso/pelis.json", "r", encoding="utf-8")
# Lectura del archivo y guardado en una string
stringArchivoPelisJSON = archivoPelisJSON.read()
# Conversión de la string anterior a un diccionario
listaDiccPelisJSON = loads(stringArchivoPelisJSON)


# Apertura para grabación de un archivo CSV (Separado por comas)
archivoPelisCSV = open("repaso/pelis.csv", "w", encoding="utf-8")

# para cada peli (que es un diccionario) en la lista de pelis obtenida de pelis.json
for peli in listaDiccPelisJSON:
    titulo = peli["Title"]
    # Actors es una string, por eso el split y luego la posición cero donde está el primer actor
    actorPrincipal = peli["Actors"].split(",")[0]
    # este es más profundo: diccionario -> lista -> diccionario -> quito el signo de porcentaje
    rating = peli["Ratings"][1]["Value"][:-1]
    # quito el signo $ y luego quito las comas
    recaudacion = peli["BoxOffice"][1:].replace(",", "")
    
    # construyo la fila con una f-string
    fila = f"{titulo},{actorPrincipal},{rating},{recaudacion}"
    # construyo la fila por concatenación
    otraFila = titulo + "," + actorPrincipal + "," + rating + "," + recaudacion
    print(fila)
    fila += "\n" # agrego el Enter para terminar la fila
    archivoPelisCSV.write(fila) # grabo la fila en el archivo

archivoPelisJSON.close()
archivoPelisCSV.close()

# Abro el CSV que grabé arriba ahora para lectura
archivoPelisCSV = open("repaso/pelis.csv", "r", encoding="utf-8")

# esta lectura construye una lista de strings (una por cada fila)
listaPelisArchivoCSV = archivoPelisCSV.readlines()

sumaRatings = 0
sumaRecaudaciones = 0

for fila in listaPelisArchivoCSV:
    _, _, rating, recaudacion = fila.split(",") # el _ reemplaza a un nombre de variable dado que no necesito esos valores (el titulo y los actores)
    sumaRatings += int(rating)
    sumaRecaudaciones += int(recaudacion)
promedioRating = sumaRatings // len(listaPelisArchivoCSV)
print(f"El rating promedio es: {promedioRating}")
print(f"La suma de las recaudaciones es: {sumaRecaudaciones}")

archivoPelisCSV.close()
