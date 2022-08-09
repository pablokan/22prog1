listaA = ["a", "b", "c"]
listaB = ["b", "b", "c", "c", "c", "a"]


listaContadores = []
for x in range(len(listaA)):
    c = 0
    for y in range(len(listaB)):
        if listaA[x] == listaB[y]:
            c += 1
    listaContadores.append(c)

print(listaContadores)

