frutas = {"manzanas": 4, "peras": 2, "frutillas": 7}

# el recorrido del diccionario sin especificar por cual elemento lo recorro, lo hace por sus claves. Es decir, es lo mismo que recorrerlo con .keys()

for elemento in frutas:
    print(elemento)

for elemento in frutas.keys():
    print(elemento)

for cantidad in frutas.values():
    print(cantidad)

for fruta, cantidad in frutas.items():
    print(fruta, cantidad)
    
