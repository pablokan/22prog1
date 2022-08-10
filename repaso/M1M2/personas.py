from json import loads

a = open("repaso/M1M2/personas.json")
s = a.read()
personas = loads(s)

def getHijos():
    lista = []
    for persona in personas:
        lista += persona["nombresHijos"]
    return lista

print(getHijos()