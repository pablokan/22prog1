numeros = []
for x in range(5):
    if x > 2:
        numeros.append(x*2)
    else:
        numeros.append(0)
print(numeros)

# comprehension list with ternary operator
num = [(x*2 if x>2 else 0) for x in range(5)]
print(num)

# recienLLego = False
# saludo = "hola" if recienLLego else "chau"
# print(saludo)

def saludo(recienLlego):
    return "hola" if recienLlego else "chau"

print(saludo(False))


