from json import loads

archivoJSON = open("vs/personas.json", "r", encoding="utf-8")
strArchivoJSON = archivoJSON.read()
dictList = loads(strArchivoJSON)

cantidadPersonas = len(dictList)
print(f"Tengo {cantidadPersonas} personas")

for persona in dictList:
    nombre = persona["nombre"]
    nombreMadre = persona["nombresPadres"]["Madre"]
    print(f"La madre de {nombre} se llama {nombreMadre}")