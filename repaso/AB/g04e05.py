# Recibir por teclado una cadena de números e insertar  un punto cada 3 dígitos como divisorio de miles. Ej.  1234567890 debería devolver 1.234.567.890

n = "123456789475895696767389505"
nNuevo = ""
posUltimoElemento = len(n)-1
c = 0
for i in range(posUltimoElemento, -1, -1):
    c += 1
    digito = n[i]
    nNuevo = digito + nNuevo
    if c == 3:
        nNuevo = "." + nNuevo
        c = 0
if nNuevo[0] == ".":
    nNuevo = nNuevo[1:]
print(nNuevo)
