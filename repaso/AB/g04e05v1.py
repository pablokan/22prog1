# Recibir por teclado una cadena de números e insertar  un punto cada 3 dígitos como divisorio de miles. Ej.  1234567890 debería devolver 1.234.567.890

n = "123456789"
nNuevo = ""

c = 0
for i in range(len(n)): # variante con rango estándar
    c += 1
    digito = n[len(n)-1-i]
    nNuevo = digito + nNuevo
    if c == 3:
        nNuevo = "." + nNuevo
        c = 0
if nNuevo[0] == ".":
    nNuevo = nNuevo[1:]
print(nNuevo)
