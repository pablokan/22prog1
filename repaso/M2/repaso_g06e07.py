# Ejemplo de funciones como
# Sub programas
# Se usa para clarificar el código

nombres = []
sexos = []

def carga():
    for i in range(3):
        nombre = input("Ingrese un nombre: ")
        sexo = input("Ingrese sexo: ")
        nombres.append(nombre)
        sexos.append(sexo)

def mostrarMujeres():
    for i in range(3):
        if sexos[i] == "f":
            print(nombres[i])

carga()
mostrarMujeres()


