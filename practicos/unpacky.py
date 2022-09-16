lista = ["Ana", 33]

def saludo(nombre, edad):
    print(f"Hola {nombre}, tenés {edad} años")

saludo("Juan", 10)
saludo(lista[0], lista[1])
saludo(*lista) # el * aqui se llama operador de unpack
saludo(lista)

