# el for va desde el valor inicial hasta el valor final menos 1
for vr in range(0, 3):  # vr es la variable de recorrido
    print("algo")
    print(vr, "- hola")
    print("nada")

valorInicial = 3
valorFinal = 7

# para la variable x en el rango desde vI hasta vF, haga lo que dice dentro
for x in range(valorInicial, valorFinal):
    print(x)

for i in range(10):  # va de 0 a 9
    print(i)
    if i == 5:
        print("ya llegó a 5!!!!!")


nombre = "nada"
while nombre != "Pablo":  # mientras la condición sea verdadera
    nombre = input("Cómo me llamo? ")
# el while termina cuando la condición se hace falsa

n = 5
while n < 10:
    print("dentro del while")
    n = n + 1  # contador n += 1

while 1 == 1:  # bucle infinito ---> cortar con Control-C
    print("infinito")
