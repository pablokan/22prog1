# Ingresar la lluvia caída en milímetros 
# para cada día de la semana. 
# Mostrar al final el total de lluvia 
# caída y el nombre del día que más llovió.

diasMasLluvioso = ""
cantidadMayorDeMm = 0
totalLluvia = 0
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
for x in range(7):
    cartel = "Ingrese MM caídos el " + dias[x] + ": "
    mm = int(input(cartel))
    totalLluvia += mm # total = total + mm
    if mm > cantidadMayorDeMm:
        cantidadMayorDeMm = mm
        diasMasLluvioso = dias[x]

print("El total de lluvia caída en la semana fue", totalLluvia)
print("El día mas lluvioso fue el", diasMasLluvioso)
