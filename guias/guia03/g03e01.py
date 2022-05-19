mayores23 = []
for i in range(5):
    n = int(input("Número: "))
    if n > 23:
        mayores23.append(n)

cantidad = len(mayores23)

print(
    "La lista de los mayores a 23 es",
    mayores23,
    "y la cantidad de los números ingresados mayores a 23 fue",
    cantidad,
)
