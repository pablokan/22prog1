# Almacenar en dos  listas paralelas, 
# nombres y sexos de 8 personas. 
# Al finalizar, recorrerlas y mostrar 
# los nombres de las mujeres. 
# Dos funciones: carga y mostrarMujeres

def carga():
    nombres = [] # variable local (solamente existe dentro de la función carga)
    sexos = []
    for x in range(3):
        nombre = input("Nombre: ")
        sexo = input("Sexo: ")
        nombres.append(nombre)
        sexos.append(sexo)
    return nombres, sexos

def mostrarMujeres(nombrecitos, sexitos):
    for x in range(len(sexitos)):
        if sexitos[x] == "f":
            print(nombrecitos[x])

ns, ss = carga() # Python permite asignación múltiple, carga devuelve dos elementos y entonces lo recibo en dos variables
# print(nombres) daría error poque nombres no existe en el programa principal
mostrarMujeres(ns, ss)
