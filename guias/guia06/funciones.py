def funcioncita(): # declaración de la función
    print("este cartelito está dentro de funcioncita")

def otraFuncion():
    return "frase retornada" # vuelve en el nombre de la función

# Programa Principal
print("Acá comienza el programa principal")
funcioncita() # call == llamada == ejecución
print("Acá sigue el programa principal")

print(otraFuncion()) # muestra el valor retornado

def saludo(nombre, edad): # nombre es un parámetro
    print("Hola", nombre, "tenés", edad, "años")

saludo("Ana", 77) # Ana es un argumento
saludo("Luis", 23)
saludo("Pipo", 11)
n = input("Cual es tu nombre: ")
e = int(input("Cual es tu edad: "))
saludo(n, e) # respetar orden, tipo de dato, cantidad






