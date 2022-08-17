def foo():
    print("yo soy la función foo")
foo()

variableNumerica = 12
variableNumerica # no muestra nada porque no la estoy printeando

def foo2():
    return "yo soy la foo2 y tengo return"
foo2() # mismo caso que la variableNumerica  
print(foo2())

def foo3():
    return "una cosa", 111, True # devuelve una tupla
print(foo3())
vString, vNumerica, vBooleana = foo3() # asigna los elementos de la tupla retornada en orden
print(f"{vNumerica=}") # contiene el 111

def foo4():
    return [1, 5, 4]
print(foo4())

def foo5():
    return 2**3
print(foo5()/2)

def foo6():
    return "Juan", 33, 1.77

nombre, edad, _ = foo6()
print(nombre)
print(foo6()[0])

nombre, _, altura = foo6()

