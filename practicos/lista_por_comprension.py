lista = []
for x in range(5):
    if x > 2:
        lista.append(x*2)

print(lista)

listaC = [x*2 for x in range(5) if x > 2]
print(listaC)

print([1,2] + [3,4])