""" def saludo(nombre, edad): # parámetros posicionale
    print(f"Hola {nombre} la mitad de tu edad es {edad/2}")
"""
#saludo(33, "Juan") # respetar la cantidad, el orden y el tipo de datos: 2 argumentos, primero una string y segundo un entero
""" 
def suma(*args):
    print(args)
    s = 0
    for e in args:
        s += e
    return s

print(suma(2, 3))
"""

# Los posicionales si existen van si o si adelante
""" def funcionQueNoSeComoLLamar(pos1, pos2, *args):
    print(pos1, pos2, args)

funcionQueNoSeComoLLamar("posicional obligatorio", 1, "q", 23, "z")
"""

def estudiante(alumno, ciudad="Río Cuarto", **kwargs):
    print(f"El alumne {alumno} es de {ciudad}.")
    if kwargs != {}: 
        print(f"Otros datos de {alumno} son: ")
        for k, v in kwargs.items():
            print(f"{k} ---> {v}")

estudiante("Juan", "San Basilio")
estudiante("Ana")
estudiante("Luisa", "Jovita", becada=True, datosValioso = "abanderada del secundario")


""" 
def foo(nominado1="algo", **kwargs):
    print(kwargs, nominado1)

foo(clave1="valor1", nominado1="otra cosa", clave2="valor2")
"""







