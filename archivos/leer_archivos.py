a = open("nombres.txt", "r", encoding="utf-8") # abre el archivo en modo lectura
""" print(f"Posición del puntero: {a.tell()}") 
b = a.read() # lee el archivo
print(f"Posición del puntero: {a.tell()}") 
print(b) # imprime el contenido del archivo
a.seek(0)

for i in range(len(b)):
    print(i, ord(b[i]), b[i])

a.seek(2) 
letraS = a.read(1) # lee un caracter
print("letra S:", letraS)
quienSabe = a.read(3)
print("quien sabe:", quienSabe)
letraN = a.read(1)
print("letra N:", letraN)
"""

lineas = a.readlines() # guarda todas las lineas en una lista
print(lineas) # ['José\n', 'Ana\n']

a.seek(0) # vuelve al principio del archivo

linea = " "
while linea != "":
    linea = a.readline() # lee una linea
    print(linea, end="") # imprime la linea

a.close() # cierra el archivo


