from json import loads

a = open("repaso/B/choto.json")
s = a.read() # construye una string con el archivo completo
listaDeDiccionarios = loads(s) # deserializa: convierte la string JSON en una lista de diccionarios de Python

for persona in listaDeDiccionarios:
    print(persona["nombre"])
    