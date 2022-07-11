# Dada una lista cargada con números enteros, obtener el promedio de ellos. Mostrar por 
# pantalla dicho promedio y los números ingresados que sean mayores que él. 
# Dos funciones: promedio y mayorQue.

lisNums = [12, 45, 1, 67, 98, 21]

def promedio(listaNumeros):
    t = 0
    for i in range(len(listaNumeros)):
        t += listaNumeros[i]
    return t/len(listaNumeros)

p = promedio(lisNums)
print(p)

def mayorQue(lista, valor):
    for i in range(len(lista)):
        if lista[i] > valor:
            print(lista[i])

mayorQue(lisNums, p)

