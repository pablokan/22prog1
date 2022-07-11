# Calcular el sueldo a cobrar teniendo en cuenta que
# los empleados que no han faltado y  cuya antigüedad
# es superior a 5 años, tienen un adicional del 30%
# sobre el sueldo básico ($47.000).
# Pedir la cantidad de días no trabajados y año de ingreso en la empresa.

diasNoTrabajados = int(input("Días no trabajados: "))
anioIngreso = int(input("Año de ingreso a la empresa: "))
sueldo = 47000
antiguedad = 2022 - anioIngreso

if diasNoTrabajados == 0 and antiguedad > 5:
    sueldo = sueldo * 1.3

print("Su sueldo es", sueldo)
