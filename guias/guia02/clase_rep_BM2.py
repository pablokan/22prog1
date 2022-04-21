# Instrucciones para controlar el flujo repetitivo (bucles o loops)
# for: para cantidades determinadas de repeticiones
# while: para cantidades indeterminadas de repeticiones

valorInicial = 3
valorFinal = 7
paso = 1
for variableDeRecorrido in range(valorInicial, valorFinal, paso):
    print("------")
    print("hola")
    print("------")

for x in range(1, 10, 2):
    print(x)

for i in range(10):
    print(i)
    if i == 5:
        print("llegó el 5!!!!")

n = 5
while n < 10:
    print("dentro del while")
    n = n + 1  # contador
print(n)

nombre = "nada"
while nombre != "Pablo":
    nombre = input("Cómo te llamás? ")

for x in range(5):
    print(x)

print("-------------------")

# Simulación de for
x = 0
while x < 5:
    print(x)
    x = x + 1
