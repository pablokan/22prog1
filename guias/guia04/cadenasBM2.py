""" nombre = "Burrito Ortega"
nombre = nombre.upper()
print(nombre)
c = 0
for i in range(len(nombre)):
    print(nombre[i])
    if nombre[i] in "AEIOU":
        c += 1
print(c)

frase = "Las noches de otoño son frescas"
posicion = frase.find("otoño")  # busca subcadena y devuelve posición
print(posicion)
otraPosicion = frase.find("s no")  # no tiene que ser una palabra
print(otraPosicion)
noExiste = frase.find("no s")  # -1 cuando no existe
print(noExiste)
print(frase.find("es"))  # encuentra el "es" de "noches"
print(
    frase.find("es", 10)
)  # encuentra el "es" de "frescas" porque empieza a buscar desde mas adelante


fecha = "3/5/2022"
listaFecha = fecha.split("/")
print(listaFecha)  # ['3', '5', '2022']

nombres = "juan---ana---pedro---luisa"
print(nombres.split("---"))  # ['juan', 'ana', 'pedro', 'luisa']

cadena = "algo otro cosa techo"
print(cadena.split()) # por defecto separa por espacio en blanco
"""

# slicing
frase = "Las noches de otoño son frescas"
print(frase[4:10])  # noches
comienzo = frase[:3]
print(comienzo)  # Las
final = frase[-7:]
final2 = frase[24:]
print(final, final2)  # frescas
print(frase[-1])

# concatenación
unaCadena = "primera cadena"
otraCadena = "segunda cadena"

nuevaCadena = unaCadena + " - " + otraCadena
print(nuevaCadena)

print(frase[333:])  # duda de Fernando
