from json import loads

archivoJSON = open("repaso/M2/pelis.json")
csvFile = open("repaso/M2/pelis.csv", "w")
stringArchivoJSON = archivoJSON.read()
archivoJSON.close()
listaPelis = loads(stringArchivoJSON)
for peli in listaPelis:
    titulo = peli["Title"]
    protagonista = peli["Actors"].split(",")[0]
    linea = f"{titulo}---{protagonista}"
    print(linea)
    csvFile.write(linea+"\n")

csvFile.close()
