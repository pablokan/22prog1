z = "hola"

def foo(s):
    s = list(s)
    s[0] = s[0].upper()
    print(s)
    s = "".join(s)
    print(s)

foo(z)
print(z)
