# Almacenar en dos  listas paralelas, 
# nombres y sexos de 8 personas. 
# Al finalizar, recorrerlas y mostrar 
# los nombres de las mujeres. 
# Dos funciones: carga y mostrarMujeres

nombres = [] # variable global (existe en todo el ámbito del programa, no están dentro de ninguna función)
sexos = []

def carga():
    for x in range(3):
        nombre = input("Nombre: ")
        sexo = input("Sexo: ")
        nombres.append(nombre)
        sexos.append(sexo)
    return nombres, sexos

def mostrarMujeres():
    for x in range(len(sexos)):
        if sexos[x] == "f":
            print(nombres[x])

carga() 
mostrarMujeres()

