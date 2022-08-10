listaDeListas = [
    [1,2,3],
    [4,5,6],
    [1,2,3],
    [4,5,6],
    [1,2,3],
    [4,5,6],
    [1,2,3],
    [4,5,6]
]

listaTotal = []
for lista in listaDeListas:
    listaTotal += lista

print(listaTotal)


a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

listaB = ["b", "b", "c", "c", "c", "a"]
print(listaB.count("c"))

nombres = ["Anana", "Luis", "Ana"]
print(nombres.count("Ana"))

print(nombres[0].count("a"))


s = "qawaeeeeaza"
print(s.count("a"))