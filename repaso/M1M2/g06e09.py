def mayorQue(lista, valor):
    for numero in lista:
        if numero > valor:
            print(numero)

mayorQue([1,2,3,4,5], 3)

listaNumeros = [5,1,4,6,2]

def promedio(cualquierListaNumeros):
    t = 0
    for n in cualquierListaNumeros:
        t += n
    return t/len(cualquierListaNumeros)


print(promedio(listaNumeros))
print(promedio([4,1,2]))

mayorQue(listaNumeros, promedio() )