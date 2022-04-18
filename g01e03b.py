# Leer un número real y emitir una leyenda informando
# si es mayor a cero, igual a cero o bien es negativo (son tres opciones).

numero = float(input("Ingrese un número real: "))

if numero > 0:
    print("es positivo")
elif numero == 0:
    print("es cero")
else:
    print("es negativo")
