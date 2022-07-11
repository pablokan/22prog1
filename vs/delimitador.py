import csv

archivo = open("datitos.txt", "r")
filas = csv.reader(archivo, delimiter="%")

print(f"{filas=}")
print("Encabezados", next(filas))
for fila in filas:
    print(fila)

archivo.close()
