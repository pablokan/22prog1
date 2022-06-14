# Diccionarios

d = {"uno": "one", "dos": 2} # pares clave-valor
print(d["dos"])
d["tres"] = 3 # agrego
print(d)
d["dos"] = "two" # modifico el valor si existe la clave, agrego si no existe la clave
print(d)
del d["uno"] # un modo de borrar
print(d)
v = d.pop("dos") # otro modo de borrar guardando el valor en otra variable común
print(d, v)

persona = {"nombre": "Juan", "edad": 21}
persona["altura"] = 1.96
personaEnLista = ["Juan", 21, 1.96] # mismo ejemplo con lista
print("La altura de", personaEnLista[0], "es", personaEnLista[2]) # solo tengo posiciones
print("La altura de", persona["nombre"], "es", persona["altura"]) # el diccionario brinda mas información
print("Antes del popitem:", persona)
# del persona["peso"] da error porque la clave no existe
persona.popitem() # elimina el último par
print("Despues del popitem:", persona)


# Recorrido por claves solas
for k in persona: # persona.keys()
    print(k)

for k, v in persona.items(): # Recorrido por item es clave y valor
    print(k, "->", v)

for v in persona.values(): # Recorrido por valor
    print(v)




