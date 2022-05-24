""" Mostrar el valor doble del número de dos cifras (que es el único número) encontrado en la cadena. Ej.: 'Juan tiene 25 años' mostraría el número 50, ‘El dólar va a llegar este mes a 57 pesos casi seguro’,  mostraría 114.
"""
# Solución Yamila
frase = 'Juan tiene 25 años'
frase = 'El dólar va a llegar este mes a 57 pesos casi seguro'
numero = ""
for i in range(len(frase)):
    if frase[i] in "1234567890":
        numero = numero + frase[i]
print(int(numero)*2)

i = 0
while frase[i] not in "123456789":
    i += 1
print(int(frase[i] + frase[i+1])*2)


