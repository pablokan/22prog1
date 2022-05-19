nombre = "Burrito Ortega"
print(nombre.upper())  # convierte la cadena a mayúsculas

c = 0
for i in range(len(nombre)):
    print(nombre[i])
    if nombre[i].upper() in "AEIOU":
        c += 1

print("Las vocales son", c)

frase = "Las noches de otoño son frescas"
posicion = frase.find("otoño")  # busca subcadena y devuelve la posición
print(posicion)
otraPosicion = frase.find("s no")
print(otraPosicion)
print(frase.find("invierno"))  # devuelve -1 porque no está
print(frase.find("es"))
print(frase.find("es", 10))  # buscar desde una posición en adelante

fecha = "2/5/2022"
# split divide la cadena por el separador y construye una lista
print(fecha.split("/"))
# el separador es la barra y la lista tendrá como elementos el día, el mes y el año

cadena = "anita---juan---lucia---pedro"
listaNombres = cadena.split("---")
print(listaNombres)

cadena2 = "patio lista comedor auto"
listaPalabras = cadena2.split()
print(listaPalabras)

# slicing
print(frase)
unaPalabra = frase[4:10]  # recorto un fragmento
print(unaPalabra)
fondo = frase[-7:]
fondo2 = frase[24:]
print(fondo, fondo2)  # son iguales
principio = frase[:3]
print(principio)

# concatenación

unaCadena = "cadena primera"
otraCadena = "cadena segunda"

nuevaCadena = unaCadena + " " + otraCadena

print(nuevaCadena)
