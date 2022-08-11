def foo():
    print("yo soy el subprograma foo")
foo()

a = 123
a

def foo2():
    return "yo soy el retorno de foo2"
foo2()
print(foo2())

def foo3():
    return "algo", 111, True
_, vNumerica, vBoleana = foo3()
print(vNumerica, vBoleana) 

vString, _, vBoleana = foo3()
print(vString, vBoleana)

def foo4():
    return [1,2,3]
lista = foo4()
print(lista)

print("Salida de foo4")
for elemento in foo4():
    print(elemento)

print("Salida de foo5")
def foo5():
    return 2**3
print(foo5()//2)

def foo6():
    return "Juan", 33
nombre, edad = foo6()
print(nombre)
print(foo6()[0])

def foo7():
    x = "hola"
    y = "chau"
    return x
print(foo7())
