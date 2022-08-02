""" s = "mal###bien###regular"
lista = s.split("###")
print(lista)

t = "hola como te va"
lista2 = t.split()
print(lista2)

w = "0123456789"
print(w[3:6])
print(w[:4])
print(w[6:])
print(w[::-3]) # -3 es el paso, va desde el fondo de 3 en 3
print(w[0:7:2]) # el 2 es el paso
 """


s = "mal###bien###regular###jdsdkljaslkd###kfskdlafj"

contador = 0
# cambiando la posición de búsqueda
posicion = s.find("###")
while posicion != -1:
    contador = contador + 1
    posicion = s.find("###", posicion + 1)
print("###" , "se repite" , contador , "veces")


s2 = "varias palabras juntas"
print(s2.upper())
print(s2.title())
print(s2.capitalize())

for letra in s2:
    print(letra, end="-")
