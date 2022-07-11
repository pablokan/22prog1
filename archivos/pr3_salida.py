from calcula_edad import edad

a = open("personas.txt", "r", encoding="utf-8")
encabezado = a.readline()
print("Los mayores de edad son los siguientes:")
for linea in a:
    nombre, fecha = linea.strip().split(",")
    if edad(fecha) >= 18:
        print(nombre)
    
a.close()
