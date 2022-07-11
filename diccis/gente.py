persona = {'nombre': 'Juan'}
# diccionario, contiene pares clave:valor
# la clave es (usualmente) una string
# el valor puede ser cualquier COSA

persona = {'nombre': 'José', "hijos": ["Katia", "Iván"], "padres": {"padre": "Juan", "madre": "Maria"}}

print(persona['hijos'])
for hijo in persona['hijos']:
    print(hijo)

print("La madre es", persona['padres']['madre'])

