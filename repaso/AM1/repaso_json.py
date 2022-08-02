from json import loads

a = open("pruebas/repaso.json")
s = a.read()
personas = loads(s)

for persona in personas:
    print(f"Nombre: {persona['nombre']}")

a.close()
