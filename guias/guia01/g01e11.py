# El costo del pasaje a Córdoba es de $2000.
# La empresa realiza un descuento de un 40 % sobre
# el costo del boleto a los niños que tienen
# entre 5 y 10 años y a los jubilados (mayores de 65).
# Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.

nombre = input("Nombre: ")
edad = int(input("Edad: "))

boleto = 2000

if 5 <= edad <= 10 or edad > 65:  # edad >=5 and edad <= 10
    boleto = boleto * 0.6

print(nombre, "paga", boleto)
