from json import loads
# Abro personas.json como cualquier archivo de texto. La extensión .json es sólo indicativa del contenido pero no es obligatoria

a = open("repaso/M2/personas.json", "r", encoding="utf-8")
# lectura para convertir el archivo en string
# no leo .readlines() porque el archivo json no tiene un formato adecuado para ser leído por líneas.
s = a.read()
a.close()
# convertir string de json a lista de diccionarios
listaDiccionarios = loads(s)

a = open("repaso/M2/personas.txt", "a")

print("Hijos de cada persona:")
for persona in listaDiccionarios:
    print("--------------------")
    nombre = persona["nombre"] 
    print(nombre)
    print("y sus hijos se llaman:")
    hijos = ""
    for hijo in persona["nombresHijos"]: 
        print(hijo)
        hijos += hijo + ", "
    hijos = hijos[:-2]

    print("y su madre se llama:")
    madre = persona["nombresPadres"]["Madre"]
    print(madre)
    linea = f"{nombre}. Hijos: {hijos}. Madre: {madre}.\n"

    a.write(linea)

a.close()
