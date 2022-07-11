# 3 bananas, 9 manzanas y 2 frutillas

def total(**kwargs):
    print(kwargs)
    t = 0
    for v in kwargs.values():
        t += v
    return t

def mayor(**kwargs):
    m = 0
    km = ""
    for k, v in kwargs.items():
        if v > m:
            m = v
            km = k
    return m, km

print(total(bananas=3, manzanas=9, frutillas=2))

cantidad, fruta = mayor(bananas=3, manzanas=9, frutillas=2)

print(f"Las {fruta} son mas y hay {cantidad}")