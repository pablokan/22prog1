class Gato:
    def __init__(self, n, e):
        self.name = n
        self.edad = e

    def __str__(self): # dunder (double underscore)
        return f"Nombre: {self.name}\nEdad: {self.edad}"

listaGatos = []

for i in range(3):
    nombreGato = input("Nombre del gato: ")
    g = Gato(nombreGato, 7)
    listaGatos.append(g)

for gatito in listaGatos:
    print(gatito)



        