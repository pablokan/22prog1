def muestraMuchasVecesHola(palabra, veces):
    for i in range(veces):
     print(palabra)
    
muestraMuchasVecesHola("hola", 4)
print()
muestraMuchasVecesHola("chau", 2)
print()
muestraMuchasVecesHola(333, 3)
p = input("Que palabra desea repetir: ")
v = int(input("Cuantas veces? "))
muestraMuchasVecesHola(p, v)


"""

def sumaYresta(a, b):
    s = a + b
    r = a - b
    return s, r

print(sumaYresta(1,4))

suma, resta = sumaYresta(3,2)
print("Suma: ", suma)
print("Resta: ", resta)

tuplaResultado = sumaYresta(300,250)
for elemento in tuplaResultado:
    print(elemento)

l = list(tuplaResultado)
print(l)
"""