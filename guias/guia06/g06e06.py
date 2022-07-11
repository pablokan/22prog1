lista = ["a", "b", "c", "d", "e", "a", "b", "c", "d", "e"]

c = 0
for x in range(len(lista)):
    if lista[x] in "aeiou":
        c += 1
print(c)
