a = open("repaso/BM2/archy.txt", "r", encoding="utf-8")
lista = a.readlines()
print(lista)
a.close()

total = 0
for persona in lista:
    print(persona)
    nombre, edad = persona.split("---") # convierto cada línea en lista
    edad = int(edad[:-1]) # le saco el Enter y lo convierto a int
    total += edad
print(total//2)

b = open("repaso/BM2/archy2.txt", "a", encoding="utf-8")
nombres = ["juan", "pedro", "ana"]
edades = [11, 22, 33]
for i in range(len(nombres)):
    linea = f"Nombre: {nombres[i]}. Edad: {edades[i]}\n"
    b.write(linea)

b.close()


