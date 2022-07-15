from json import loads

a = open("repaso/B/personas.json", "r", encoding="utf-8")
s = a.read()
a.close()

listaPersonas = loads(s)

a = open("repaso/B/personas.txt", "a", encoding="utf-8")
for persona in listaPersonas:
    nombre =persona["nombre"]
    listaHijos = persona["nombresHijos"]
    hijos = ""
    for hijo in listaHijos:
        hijos += hijo + ", "
    hijos = hijos[:-2]
    madre = persona["nombresPadres"]["Madre"]
    linea = f"{nombre}. Hijos: {hijos}. Madre: {madre}."
    print(linea)
    a.write(linea+"\n")



a.close()
