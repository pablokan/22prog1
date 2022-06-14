def mayorCantidad(**kwargs):
    m = 0
    for k, v in kwargs.items():
        if v > m:
            m = v
            o = k
    return o, m

print(mayorCantidad(banana=3, manzana=9, frutilla=2))

def suma(**kwargs):
    t = 0

suma(banana=3, manzana=9, frutilla=2)

def displayData(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} ---> {v}")

displayData()
