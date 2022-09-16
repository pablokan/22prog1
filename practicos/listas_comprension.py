# comprehension lists

lista = []
for x in range(5):
    if x > 2:
     lista.append(x*2)
print(lista)

lista2 = [x*2 for x in range(5) if x > 2]
print(lista2)

a = [1, 2]
b = [3, 4]
print(a+b)