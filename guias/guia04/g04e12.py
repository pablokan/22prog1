# Mostrar el valor doble del número de dos cifras (que es el único número) 
# encontrado en la cadena. 
# Ej.: 'Juan tiene 25 años' mostraría el número 50, 
# ‘El dólar va a llegar este mes a 57 pesos casi seguro’,  mostraría 114.

f = 'Juan tiene 25 años'
f = 'El dólar va a llegar este mes a 57 pesos casi seguro'
digitos = "123456789"
c = 0
while f[c] not in digitos:
    c += 1

print(int(f[c] + f[c+1])*2)
