def foo():
    return 1+2

a = foo()
b = foo() + 65
print(b, a, foo())

def bar():
    q = 2 + 3
    print(q)

z = bar()
print(z) # z no vale nada porque bar() no retorna

