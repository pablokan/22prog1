def suma(*args):
    print(*args)
    print(f"{args=}")
    t = 0
    for e in args:
        t += e
    return t

li = [1,2,3]
print(*li)

print(suma(3,4))
print(suma(*li))

num = 123.4567
print(f"{num:.2f}")
print(f"{num * 2 = }")
nestedFormat3 = ".3f"
print(f"{num:{nestedFormat3}}")

