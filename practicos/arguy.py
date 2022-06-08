""" def foo(*args):
    for e in args:
        print(e)

foo("hola", "nombre")
foo(1,2,3,4,4,5, True)

def suma(*args):
    t = 0
    for e in args:
        t += e
    return t

print(suma(3,3,4,4))
print(suma(3.3,3.1,42,43, 55,77,344))
print(suma(3,"q"))
 """

def foo():
    return 1, 2

a = foo()
print(a)
for e in a:
    print(e)

for x in range(len(a)):
    print(a[x])








