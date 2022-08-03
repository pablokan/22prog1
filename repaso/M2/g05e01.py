cadena = "Juan$120000,Ana$250000,Luis$76500,Vilma$98700"

lista = cadena.split(",")
print(lista)
nombres = []
sueldos = []

for persona in lista:
    nombre, sueldo = persona.split("$")
    nombres.append(nombre)
    sueldos.append(int(sueldo))

print(nombres)
print(sueldos)
