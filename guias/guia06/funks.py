def funcioncita(): # declaración de la función
    print("esto está dentro de funcioncita")

def otraFuncion():
    return "frase retornada"

def devuelveCuadrado():
    n = 3 * 3
    return n

# Programa Principal
print("Primera cosa que pasa en este programa")
funcioncita() # llamada == call == ejecución
print("Después de la llamada a funcioncita")
print(otraFuncion()) # el valor de retorno vuelve en el nombre de la función
print("=============")
devuelveCuadrado() # no hace nada, es como poner una variable sin printearla
print("=============")
z = devuelveCuadrado()
print(z)

def saludo(nombre, edad): # nombre es un parámetro
    print("Hola", nombre, "tenés", edad, "años") # el parámetro se comporta como una variable

saludo("Ana", 77) # "Ana" es un argumento que se le pasa a la función
saludo("Luis", 12) # mismo orden, cantidad y tipo de dato
saludo("Vilma", 22)
n = input("Ingrese su nombre: ")
e = int(input("Ingrese su edad: "))
saludo(n, e)







