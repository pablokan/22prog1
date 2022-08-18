class Gato:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def __str__(self):
        return f"Soy un gatito llamado {self.nombre} y tengo {self.edad} años"

listaGatitos = []
for i in range(3):
    no = input("Nombre del gatito: ")
    ed = int(input("Edad del gatito: "))
    g = Gato(no, ed)
    listaGatitos.append(g)

for gatito in listaGatitos:
    print(gatito)

