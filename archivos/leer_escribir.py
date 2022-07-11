a = open("archivos/texto.txt", "r+")
cA = a.read().count("*")
a.write(f"La cantidad de asteriscos es {cA}")

a.close()
